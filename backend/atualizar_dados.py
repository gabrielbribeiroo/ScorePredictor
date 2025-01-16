# Script Python para buscar dados da API e salvar no arquivo Prolog.
import requests

API_KEY = 'SUA_CHAVE_API'
BASE_URL = 'https://v3.football.api-sports.io'

HEADERS = {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': API_KEY
}

def obter_dados_brasileirao(temporada):
    """Obtém os dados do Brasileirão para uma temporada específica."""
    url = f"{BASE_URL}/standings?league=71&season={temporada}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar dados:", response.status_code, response.text)
        return None

def calcular_aproveitamento(jogos):
    """Calcula o aproveitamento baseado em uma lista de resultados."""
    pontos_conquistados = sum([3 if r == 'W' else 1 if r == 'D' else 0 for r in jogos])  # 'W' = vitória, 'D' = empate, 'L' = derrota
    total_jogos = len(jogos)
    return round((pontos_conquistados / (total_jogos * 3)) * 100, 2) if total_jogos > 0 else 0

def salvar_dados_em_prolog(dados, arquivo):
    """Salva os dados obtidos em um arquivo Prolog."""
    times = dados['response'][0]['league']['standings'][0]
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write('% Dados atualizados dos times do Brasileirão\n\n')
        
        for time in times:
            nome = time['team']['name'].lower().replace(' ', '_')
            
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
            classificacao = time['rank']
            gols_pro = time['all']['goals']['for']
            gols_contra = time['all']['goals']['against']
            posse_bola = 50  # Valor fixo se não disponível na API
            chutes_gol = 5  # Valor fixo se não disponível na API
            chutes_fora = 5  # Valor fixo se não disponível na API
            vitorias = time['all']['win']
            
            # Resultados recentes e aproveitamentos
            ultimos_5_jogos = [match['result'] for match in time['form'][:5]]  # Obtém os últimos 5 resultados ('W', 'D', 'L')
            aprov_rec = calcular_aproveitamento(ultimos_5_jogos)
            
            jogos_casa = [match['result'] for match in time['home']['results']]  # Resultados em casa
            aprov_casa = calcular_aproveitamento(jogos_casa)
            
            jogos_fora = [match['result'] for match in time['away']['results']]  # Resultados fora de casa
            aprov_fora = calcular_aproveitamento(jogos_fora)
            
            # Grava os dados no arquivo Prolog
            f.write(f"time({nome}, {status}, {classificacao}, {gols_pro}, {gols_contra}, {posse_bola}, {chutes_gol}, {chutes_fora}, {vitorias}, {aprov_rec}, {aprov_casa}, {aprov_fora}, 0.2).\n")

if __name__ == "__main__":
    temporada = 2025
    dados = obter_dados_brasileirao(temporada)
    if dados:
        salvar_dados_em_prolog(dados, 'prolog/dados.pl')
        print("Dados salvos com sucesso em prolog/dados.pl")
    else:
        print("Falha ao obter os dados do Brasileirão.")