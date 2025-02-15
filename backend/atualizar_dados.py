# Script Python para buscar dados da API e salvar no arquivo Prolog.
import requests

API_KEY = 'live_09e4c59f81eb4e8d7598afc5922efc'
BASE_URL = 'https://api.api-futebol.com.br/v1/campeonatos/6'

HEADERS = {
    'Authorization': f'Bearer {API_KEY}'  # Corrigido para o formato correto
}

def obter_dados_brasileirao():
    """Obtém os dados do Brasileirão."""
    url = f"{BASE_URL}/tabela"  # Corrigido para o endpoint correto
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar dados:", response.status_code, response.text)
        return None

def calcular_aproveitamento(vitorias, jogos):
    """Calcula o aproveitamento baseado em vitórias e total de jogos."""
    return round((vitorias / jogos) * 100, 2) if jogos > 0 else 0

def salvar_dados_em_prolog(dados, arquivo):
    """Salva os dados obtidos em um arquivo Prolog."""
    times = dados  # A API já retorna a tabela diretamente
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write('% Dados atualizados dos times do Brasileirão\n\n')
        
        for time in times:
            nome = time['time']['nome_popular'].lower().replace(' ', '_')
            
            # Classificação dos times por status
            if nome in ['atletico-mg', 'botafogo', 'corinthians', 'cruzeiro', 'flamengo', 'fluminense', 'grêmio', 'internacional', 'palmeiras', 'santos', 'sao_paulo', 'vasco']:
                status = "grande"
            elif nome in ['bahia', 'bragantino', 'ceara', 'fortaleza', 'sport']:
                status = "medio"
            elif nome in ['juventude', 'mirassol', 'vitoria']:
                status = "pequeno"
            else:
                status = "desconhecido"
            
            # Dados básicos
            classificacao = time['posicao']
            gols_pro = time['gols_pro']
            gols_contra = time['gols_contra']
            vitorias = time['vitorias']
            jogos = time['jogos']
            
            # Valores fixos para posse de bola e chutes
            posse_bola = 50
            chutes_gol = 5
            chutes_fora = 5
            
            # Aproveitamento
            aprov_geral = calcular_aproveitamento(vitorias, jogos)
            aprov_casa = aprov_geral  # Sem API específica, usando o geral
            aprov_fora = aprov_geral  # Sem API específica, usando o geral

            # Grava os dados no arquivo Prolog
            f.write(f"time({nome}, {status}, {classificacao}, {gols_pro}, {gols_contra}, {posse_bola}, {chutes_gol}, {chutes_fora}, {vitorias}, {aprov_geral}, {aprov_casa}, {aprov_fora}, 0.2).\n")

if __name__ == "__main__":
    dados = obter_dados_brasileirao()
    if dados:
        salvar_dados_em_prolog(dados, 'prolog/dados.pl')
        print("Dados salvos com sucesso em prolog/dados.pl")
    else:
        print("Falha ao obter os dados do Brasileirão.")