const homeTeamSelect = document.getElementById("homeTeam");
const awayTeamSelect = document.getElementById("awayTeam");
const resultsSection = document.getElementById("results");

// Buscar times da API
async function loadTeams() {
    const response = await fetch("/api/teams");
    const teams = await response.json();

    // Preencher os dropdowns com os times
    Object.keys(teams).forEach(team => {
        const optionHome = document.createElement("option");
        optionHome.value = team;
        optionHome.textContent = team.replace("_", " ").toUpperCase();

        const optionAway = optionHome.cloneNode(true);

        homeTeamSelect.appendChild(optionHome);
        awayTeamSelect.appendChild(optionAway);
    });
}

// Calcular as probabilidades
async function calculateProbabilities() {
    const homeTeam = homeTeamSelect.value;
    const awayTeam = awayTeamSelect.value;

    const response = await fetch("/api/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ home_team: homeTeam, away_team: awayTeam })
    });

    const data = await response.json();

    if (data.error) {
        resultsSection.innerHTML = `<p>Erro: ${data.error}</p>`;
    } else {
        resultsSection.innerHTML = `
            <p>Probabilidade de ${data.home_team.replace("_", " ")} vencer: ${data.prob_home}%</p>
            <p>Probabilidade de ${data.away_team.replace("_", " ")} vencer: ${data.prob_away}%</p>
            <p>Probabilidade de empate: ${data.prob_draw}%</p>
        `;
    }

    resultsSection.scrollIntoView({ behavior: "smooth" });
}

document.getElementById("calculateButton").addEventListener("click", calculateProbabilities);

// Carregar times ao carregar a página
loadTeams();