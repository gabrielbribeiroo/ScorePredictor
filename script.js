const apiKey = 'live_09e4c59f81eb4e8d7598afc5922efc';
const baseUrl = 'https://api.api-futebol.com.br/v1/campeonatos/6';

const headers = {
    'Authorization': `Bearer ${apiKey}` // A API usa Bearer Token, não x-rapidapi-key
};

// Função para carregar os times do Campeonato Brasileiro 2025
const fetchTeams = async () => {
    try {
        const response = await fetch(`${baseUrl}/campeonatos/10/tabela`, { headers });
        if (!response.ok) throw new Error(`Erro na requisição: ${response.status}`);

        const teamsData = await response.json();
        const homeSelect = document.getElementById('homeTeam');
        const awaySelect = document.getElementById('awayTeam');

        teamsData.forEach(team => {
            const option = document.createElement('option');
            option.value = team.time.nome_popular.toLowerCase().replace(" ", "_");
            option.textContent = team.time.nome_popular;

            homeSelect.appendChild(option.cloneNode(true));
            awaySelect.appendChild(option);
        });
    } catch (error) {
        console.error('Erro ao buscar os times:', error);
    }
};

// Aguarda o carregamento da página para executar o script
document.addEventListener("DOMContentLoaded", fetchTeams);