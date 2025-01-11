:- use_module(library(http/http_server)).
:- use_module(library(http/json)).

:- consult('dados.pl').

% Endpoint para prever resultados
:- http_handler(root(api/prever_resultado), handle_prever_resultado, []).

handle_prever_resultado(Request) :-
    http_read_json_dict(Request, Dict),
    Dict.homeTeam = HomeTeam,
    Dict.awayTeam = AwayTeam,
    Dict.homeDesfalque = HomeDesfalque,
    Dict.awayDesfalque = AwayDesfalque,

    % Calcular probabilidades
    prever_resultado(HomeTeam, AwayTeam, ProbCasa, ProbFora, ProbEmpate, HomeDesfalque, AwayDesfalque),

    % Retornar resposta JSON
    reply_json_dict(_{
        ProbCasa: ProbCasa,
        ProbFora: ProbFora,
        ProbEmpate: ProbEmpate
    }).

% Iniciar servidor
:- initialization(http_server([port(8080)])). 