
const apiKey = 'd7aa2b611b6d75eb3e07115169e4f744'; 
const baseUrl = 'https://v3.football.api-sports.io';

const headers = {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': apiKey
};

// Função para carregar os times do Brasileirão Série A 2025
const fetchTeams = async () => {
    try {
        const response = await axios.get(`${baseUrl}/teams?league=71&season=2025`, { headers });
        const teams = response.data.response;
        const homeSelect = document.getElementById('home-team');
        const awaySelect = document.getElementById('away-team');

        teams.forEach(team => {
        const option = `<option value="${team.team.id}">${team.team.name}</option>`;
        homeSelect.innerHTML += option;
        awaySelect.innerHTML += option;
        });
    } 
    catch (error) {
        console.error('Erro ao buscar os times:', error);
    }
};

// Função para prever o resultado da partida (simulação)
const predict = async () => {
    const homeTeam = document.getElementById('home-team').value;
    const awayTeam = document.getElementById('away-team').value;
    const homeAbsence = document.getElementById('home-absence').value;
    const awayAbsence = document.getElementById('away-absence').value;

    try {
        const response = await axios.post('https://api.example.com/predict', { // Substitua com a URL correta da API de previsão
        homeTeam, 
        awayTeam, 
        homeAbsence, 
        awayAbsence
        });

        document.getElementById('results').innerHTML = `
        <p>Vitória Mandante: ${response.data.homeWin}%</p>
        <p>Empate: ${response.data.draw}%</p>
        <p>Vitória Visitante: ${response.data.awayWin}%</p>
        `;
    } 
    catch (error) {
        console.error('Erro ao prever a partida:', error);
    }
};

document.getElementById('predict-btn').addEventListener('click', predict);

// Carrega os times ao carregar a página
fetchTeams();