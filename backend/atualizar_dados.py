# Script Python para buscar dados da API e salvar no arquivo Prolog.
import requests

API_KEY = 'SUA_CHAVE_API'
BASE_URL = 'https://v3.football.api-sports.io'

HEADERS = {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': API_KEY
}

def obter_dados_brasileirao(temporada):
    url = f"{BASE_URL}/standings?league=71&season={temporada}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar dados:", response.status_code, response.text)
        return None

def salvar_dados_em_prolog(dados, arquivo):
    times = dados['response'][0]['league']['standings'][0]
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write('% Dados atualizados dos times do Brasileirão\n\n')
        
        for time in times:
            nome = time['team']['name'].lower().replace(' ', '_')
            if nome in ['atletico-mg', 'botafogo', 'corinthians', 'cruzeiro', 'flamengo', 'fluminense', 'grêmio', 'internacional', 'palmeiras', 'santos', 'sao_paulo', 'vasco']:
                status = "grande"
            elif nome in ['bahia', 'bragantino', 'ceara', 'fortaleza', 'sport']:
                status = "medio"
            elif nome in ['juventude', 'mirassol', 'vitoria']:
                status = "pequeno"
            else:
                status = "desconhecido"  # Caso o time não esteja listado.
            classificacao = time['rank']
            gols_pro = time['all']['goals']['for']
            gols_contra = time['all']['goals']['against']
            posse_bola = 50
            chutes_gol = 5
            chutes_fora = 5
            vitorias = time['all']['win']
            aprov_rec = round((vitorias / 38) * 100, 2)
            aprov_casa = aprov_rec * 1.1
            aprov_fora = aprov_rec * 0.9
            
            f.write(f"time({nome}, {status}, {classificacao}, {gols_pro}, {gols_contra}, {posse_bola}, {chutes_gol}, {chutes_fora}, {vitorias}, {aprov_rec}, {aprov_casa}, {aprov_fora}, 0.2).\n")

if __name__ == "__main__":
    temporada = 2025
    dados = obter_dados_brasileirao(temporada)
    if dados:
        salvar_dados_em_prolog(dados, 'prolog/dados.pl')
        print("Dados salvos com sucesso em prolog/dados.pl")
