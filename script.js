const apiKey = 'live_09e4c59f81eb4e8d7598afc5922efc'; // Sua chave da API-Futebol
const baseUrl = 'https://api.api-futebol.com.br/v1';

// Função para buscar os times do Campeonato Paulista 2025
const fetchTeams = async () => {
    try {
        const response = await fetch(`${baseUrl}/campeonatos/83/times`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${apiKey}`
            }
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();
        console.log("🔍 Dados da API:", data); // Verificando os dados no console

        const homeSelect = document.getElementById('homeTeam'); // Corrigido o ID
        const awaySelect = document.getElementById('awayTeam'); // Corrigido o ID

        homeSelect.innerHTML = '<option value="" disabled selected>Selecione o Time</option>';
        awaySelect.innerHTML = '<option value="" disabled selected>Selecione o Time</option>';

        data.times.forEach(team => {
            const option = `<option value="${team.id}">${team.nome_popular}</option>`;
            homeSelect.innerHTML += option;
            awaySelect.innerHTML += option;
        });

    } catch (error) {
        console.error("❌ Erro ao buscar os times:", error);
    }
};

// Aguarda o carregamento do DOM antes de executar a função
document.addEventListener("DOMContentLoaded", fetchTeams);