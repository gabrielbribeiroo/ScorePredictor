import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurações da API de futebol
API_KEY = "e5c6e061715e09edeb441c6c8e0da104"
BASE_URL = "https://api.football-data.org/v4/competitions/CPA/standings"  # Alterado para Campeonato Paulista

# Função para buscar dados dos times
def fetch_teams_data():
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code != 200:
        return {"error": "Não foi possível buscar os dados dos times"}
    
    data = response.json()
    teams = {}
    
    # Processar os dados para extrair informações dos times
    for team_entry in data["standings"][0]["table"]:
        team_name = team_entry["team"]["name"].lower().replace(" ", "_")
        teams[team_name] = {
            "status": "grande" if team_entry["position"] <= 6 else ("medio" if team_entry["position"] <= 14 else "pequeno"),
            "classificacao": team_entry["position"],
            "gols_pro": team_entry["goalsFor"],
            "gols_contra": team_entry["goalsAgainst"],
            "posse_bola": 0,  # Dados de posse podem ser carregados de outra API
            "vitorias": team_entry["won"]
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
    prob_home = (home_stats["classificacao"] + home_stats["vitorias"]) * 1.2
    prob_away = (away_stats["classificacao"] + away_stats["vitorias"]) * 1.0
    total = prob_home + prob_away + 10  # Ajuste para empate
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
    app.run(debug=True)