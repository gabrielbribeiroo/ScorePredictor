import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurações da API de futebol
API_KEY = "live_09e4c59f81eb4e8d7598afc5922efc"
BASE_URL = "https://api.api-futebol.com.br/v1/campeonatos/6"

# Função para buscar dados dos times
def fetch_teams_data():
    headers = {"Authorization": f"Bearer {API_KEY}"}  # Corrigido para Bearer Token
    try:
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()  # Lança erro caso o status seja diferente de 200
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao buscar dados: {str(e)}"}
    
    data = response.json()

    if "tabela" not in data:
        return {"error": "Estrutura da API inesperada"}

    teams = {}

    # Processar os dados para extrair informações dos times
    for team_entry in data["tabela"]:
        team_name = team_entry["time"]["nome_popular"].lower().replace(" ", "_")
        teams[team_name] = {
            "status": "grande" if team_entry["posicao"] <= 6 else ("medio" if team_entry["posicao"] <= 14 else "pequeno"),
            "classificacao": team_entry["posicao"],
            "gols_pro": team_entry["gols_pro"],
            "gols_contra": team_entry["gols_contra"],
            "posse_bola": 0,  # Dados de posse podem ser carregados de outra API
            "vitorias": team_entry["vitorias"]
        }

    return teams

# Endpoint para obter os dados dos times
@app.route("/api/teams", methods=["GET"])
def get_teams():
    teams_data = fetch_teams_data()
    if "error" in teams_data:
        return jsonify(teams_data), 500
    return jsonify(teams_data)

# Endpoint para calcular as probabilidades
@app.route("/api/calculate", methods=["POST"])
def calculate_probabilities():
    data = request.json
    home_team = data.get("home_team")
    away_team = data.get("away_team")

    teams_data = fetch_teams_data()
    if "error" in teams_data:
        return jsonify(teams_data), 500
    
    home_stats = teams_data.get(home_team)
    away_stats = teams_data.get(away_team)

    if not home_stats or not away_stats:
        return jsonify({"error": "Time não encontrado"}), 404

    # Simulação de cálculo de probabilidade com base nos dados
    prob_home = (21 - home_stats["classificacao"]) * 1.2 + home_stats["vitorias"] * 1.5
    prob_away = (21 - away_stats["classificacao"]) * 1.0 + away_stats["vitorias"] * 1.5
    total = prob_home + prob_away + 15  # Ajuste para empate

    prob_home_percent = (prob_home / total) * 100
    prob_away_percent = (prob_away / total) * 100
    prob_draw_percent = 100 - (prob_home_percent + prob_away_percent)

    return jsonify({
        "home_team": home_team,
        "away_team": away_team,
        "prob_home": round(prob_home_percent, 2),
        "prob_away": round(prob_away_percent, 2),
        "prob_draw": round(prob_draw_percent, 2),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Permite execução externa