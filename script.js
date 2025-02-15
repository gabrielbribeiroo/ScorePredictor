const apiKey = 'live_09e4c59f81eb4e8d7598afc5922efc';
const baseUrl = 'https://api.api-futebol.com.br/v1/campeonatos/10';

const headers = {
    'x-apisports-key': apiKey  // Corrigido o cabeçalho correto
};

// Função para carregar os times do Campeonato Paulista 2025
const fetchTeams = async () => {
    try {
        const response = await axios.get(`${baseUrl}/teams?league=83&season=2025`, { headers });
        const teams = response.data.response;
        const homeSelect = document.getElementById('home-team');
        const awaySelect = document.getElementById('away-team');

        teams.forEach(team => {
            const option = document.createElement('option');
            option.value = team.team.name.toLowerCase().replace(" ", "_");  // Padrão para a API Flask
            option.textContent = team.team.name;
            homeSelect.appendChild(option.cloneNode(true));
            awaySelect.appendChild(option);
        });
    } catch (error) {
        console.error('Erro ao buscar os times:', error);
    }
};

// Função para prever o resultado da partida (simulação)
const predict = async () => {
    const homeTeam = document.getElementById('home-team').value;
    const awayTeam = document.getElementById('away-team').value;

    if (!homeTeam || !awayTeam) {
        alert("Por favor, selecione os dois times.");
        return;
    }

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/calculate', { 
            home_team: homeTeam,  // Corrigido para corresponder à API Flask
            away_team: awayTeam
        });

        document.getElementById('results').innerHTML = `
            <p>Vitória Mandante: ${response.data.prob_home}%</p>
            <p>Empate: ${response.data.prob_draw}%</p>
            <p>Vitória Visitante: ${response.data.prob_away}%</p>
        `;
    } catch (error) {
        console.error('Erro ao prever a partida:', error);
        document.getElementById('results').innerHTML = `<p style="color: red;">Erro ao obter previsão.</p>`;
    }
};

document.getElementById('predict-btn').addEventListener('click', predict);

// Carrega os times ao carregar a página
fetchTeams();