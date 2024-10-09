% Carregar os dados
:- consult('dados.pl').

% Definir os pesos ajustados para cada critério
pesos_ajustados(Pesos) :- 
    Pesos = [
        gols_pro-0.2,
        gols_contra-(-0.2),
        posse_bola-0.05,
        chutes_gol-0.06,
        chutes_fora-0.03,
        vitorias-0.2,
        classificacao-(-0.25),
        time_grande-0.2,
        time_medio-0.14,
        time_pequeno-0.1,
        aprovrec-0.25
    ].

% Mapeamento de desfalques para fatores de ajuste
fator_desfalque(completo, 1.0).
fator_desfalque(pouco_desfalcado, 0.90).
fator_desfalque(desfalcado, 0.80).
fator_desfalque(muito_desfalcado, 0.70).

% Função para calcular a contribuição de cada time com base nos critérios e pesos, ajustando pelo desfalque
calcular_contribuicao(Time, Contribuicao, FatorCasa, Desfalque) :-
    time(Time, Status, Classificacao, GolsPro, GolsContra, PosseBola, ChutesGol, ChutesFora, Vitorias, AprovRec, AprovCasa, AprovFora, _FatorCasaFora),
    pesos_ajustados(Pesos),
    member(gols_pro-PesoGolsPro, Pesos),
    member(gols_contra-PesoGolsContra, Pesos),
    member(posse_bola-PesoPosse, Pesos),
    member(chutes_gol-PesoChutesGol, Pesos),
    member(chutes_fora-PesoChutesFora, Pesos),
    member(vitorias-PesoVitorias, Pesos),
    member(classificacao-PesoClassificacao, Pesos),
    member(aprovrec-PesoAprovRec, Pesos),
    (Status == grande -> member(time_grande-PesoStatus, Pesos);
     Status == medio -> member(time_medio-PesoStatus, Pesos);
     member(time_pequeno-PesoStatus, Pesos)),
    
    % Aplicar o aproveitamento correto dependendo se é casa ou fora
    (FatorCasa == true -> FatorAprov = AprovCasa; FatorAprov = AprovFora),
    
    % Calculo utilizando as estatísticas e seus respectivos pesos
    ContribuicaoBasica is GolsPro * PesoGolsPro +
                         GolsContra * PesoGolsContra +
                         PosseBola * PesoPosse +
                         ChutesGol * PesoChutesGol +
                         ChutesFora * PesoChutesFora +
                         Vitorias * PesoVitorias +
                         Classificacao * PesoClassificacao +
                         AprovRec * PesoAprovRec +  
                         FatorAprov * PesoAprovRec +
                         PesoStatus,

    % Multiplicar a contribuição da casa pelo fator 1.2
    (FatorCasa == true -> ContribuicaoCasaAjustada is ContribuicaoBasica * 1.2; ContribuicaoCasaAjustada = ContribuicaoBasica),
    
    % Aplicar o impacto dos desfalques da mesma forma que o fator casa
    fator_desfalque(Desfalque, FatorDesfalque),
    Contribuicao is ContribuicaoCasaAjustada * FatorDesfalque.

% Ajuste dinâmico para clássicos
ajustar_para_classico(StatusCasa, StatusFora, ContribuicaoCasa, ContribuicaoFora, ContribuicaoCasaAjustada, ContribuicaoForaAjustada, MaxEmpateAjustado) :-
    ( (StatusCasa == grande, StatusFora == grande) ; 
      (StatusCasa == medio, StatusFora == medio) ; 
      (StatusCasa == pequeno, StatusFora == pequeno) ),
    !,  % Se for um clássico, ajusta as contribuições para serem mais equilibradas
    FatorAjuste is 0.95,  % Suaviza a diferença em clássicos
    ContribuicaoCasaAjustada is ContribuicaoCasa * FatorAjuste,
    ContribuicaoForaAjustada is ContribuicaoFora * FatorAjuste,
    MaxEmpateAjustado is 40.  % Aumenta a probabilidade de empate em clássicos.
ajustar_para_classico(_, _, ContribuicaoCasa, ContribuicaoFora, ContribuicaoCasa, ContribuicaoFora, 35).  % Para jogos normais, mantém as contribuições e o empate padrão.

% Cálculo da probabilidade de empate com ajuste retirando do visitante
calcular_probabilidade_com_empate(ContribuicaoCasa, ContribuicaoFora, MaxEmpate, ProbEmpate, ProbForaAjustado) :-
    Diferenca is abs(ContribuicaoCasa - ContribuicaoFora),
    
    % Reduzir uma fração da vantagem do visitante e transferir para o empate
    AjusteEmpate is min(10, (Diferenca / (ContribuicaoCasa + ContribuicaoFora)) * 10),
    ProbEmpate is min(MaxEmpate, AjusteEmpate + ((1 - Diferenca / (ContribuicaoCasa + ContribuicaoFora)) * MaxEmpate)),
    
    % Retirar parte da vantagem do visitante e transferir para o empate
    ProbForaAjustado is max(1, (ContribuicaoFora / (ContribuicaoCasa + ContribuicaoFora)) * (100 - ProbEmpate)).

% Função para calcular a probabilidade final de vitória e empate
prever_resultado(TimeCasa, TimeFora, ProbCasa, ProbFora, ProbEmpateFinal, DesfalqueCasa, DesfalqueFora) :-
    time(TimeCasa, StatusCasa, _, _, _, _, _, _, _, _, _, _, _),
    time(TimeFora, StatusFora, _, _, _, _, _, _, _, _, _, _, _),
    calcular_contribuicao(TimeCasa, ContribuicaoCasa, true, DesfalqueCasa),  % Time da casa com ajuste de desfalque
    calcular_contribuicao(TimeFora, ContribuicaoFora, false, DesfalqueFora),  % Time de fora com ajuste de desfalque
    ajustar_para_classico(StatusCasa, StatusFora, ContribuicaoCasa, ContribuicaoFora, ContribuicaoCasaAjustada, ContribuicaoForaAjustada, MaxEmpateAjustado),
    calcular_probabilidade_com_empate(ContribuicaoCasaAjustada, ContribuicaoForaAjustada, MaxEmpateAjustado, ProbEmpateAjustado, ProbForaAjustada),
    TotalContribuicao is ContribuicaoCasaAjustada + ContribuicaoForaAjustada,
   
    % Calcular as probabilidades de cada time
    ProbCasaRaw is (ContribuicaoCasaAjustada / TotalContribuicao) * (100 - ProbEmpateAjustado),
   
    % Ajuste para garantir que a soma seja exatamente 100%
    SomaBruta is ProbCasaRaw + ProbForaAjustada + ProbEmpateAjustado,
    FatorAjuste is 100 / SomaBruta,  % Ajustar as probabilidades para somarem 100%
    ProbCasaAjustada is ProbCasaRaw * FatorAjuste,
    ProbFora is ProbForaAjustada * FatorAjuste,
    ProbEmpateAjustadoFinal is ProbEmpateAjustado * FatorAjuste,

    % Garantir que todas as probabilidades sejam no mínimo 1%
    ProbCasa is max(1, ProbCasaAjustada),
    ProbEmpateFinal is max(1, ProbEmpateAjustadoFinal).

% Interação com o usuário para prever resultado
consultar_jogo :- 
    format('----------------------------------------------------------------------------------------------------~n'),
    format('                                            MENU DA PARTIDA                                         ~n'),
    format('----------------------------------------------------------------------------------------------------~n'),
    format('                                      SITUACAO DOS TIMES                                            ~n'),
    format('completo [0-1 desfalques]~npouco_desfalcado [2-3 desfalques]~n'),
    format('desfalcado [4 DESFALQUES]~nmuito_desfalcado [5+ desfalques]~n'),
    format('----------------------------------------------------------------------------------------------------~n'),
    write('Digite o time da casa: '), 
    read(TimeCasaStr), downcase_atom(TimeCasaStr, TimeCasa), 
    write('Digite o time de fora: '), 
    read(TimeForaStr), downcase_atom(TimeForaStr, TimeFora),
    
    % Perguntar sobre o nível de desfalque dos times
    format('----------------------------------------------------------------------------------------------------~n'),
    write('O time da casa esta completo, pouco_desfalcado, desfalcado ou muito_desfalcado? '),
    read(DesfalqueCasaStr), downcase_atom(DesfalqueCasaStr, DesfalqueCasa),
    write('O time de fora esta completo, pouco_desfalcado, desfalcado ou muito_desfalcado? '),
    read(DesfalqueForaStr), downcase_atom(DesfalqueForaStr, DesfalqueFora),
    format('====================================================================================================~n'),
    prever_resultado(TimeCasa, TimeFora, ProbCasa, ProbFora, ProbEmpate, DesfalqueCasa, DesfalqueFora),
    
    % Exibir as probabilidades
    format('Probabilidade de ~w ganhar: ~2f%~n', [TimeCasa, ProbCasa]),
    format('Probabilidade de ~w ganhar: ~2f%~n', [TimeFora, ProbFora]),
    format('Probabilidade de empate: ~2f%~n', [ProbEmpate]),
    format('====================================================================================================~n').