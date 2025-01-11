document.getElementById("predict-button").addEventListener("click", async () => {
    // Obtenha os valores inseridos no formulário
    const homeTeam = document.getElementById("home-team").value.trim();
    const awayTeam = document.getElementById("away-team").value.trim();
    const homeCondition = document.getElementById("home-condition").value;
    const awayCondition = document.getElementById("away-condition").value;

    // Valide os campos
    if (!homeTeam || !awayTeam) {
        alert("Por favor, insira os nomes dos times.");
        return;
    }

    try {
        // Envie os dados para a API
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                home_team: homeTeam,
                away_team: awayTeam,
                home_condition: homeCondition,
                away_condition: awayCondition,
            }),
        });

        // Verifique se a API respondeu corretamente
        if (!response.ok) {
            throw new Error("Erro ao obter os resultados. Verifique se a API está em execução.");
        }

        const result = await response.json();

        // Exiba os resultados
        document.getElementById("home-probability").textContent = `Probabilidade de vitória do ${homeTeam}: ${result.prob_home}%`;
        document.getElementById("away-probability").textContent = `Probabilidade de vitória do ${awayTeam}: ${result.prob_away}%`;
        document.getElementById("draw-probability").textContent = `Probabilidade de empate: ${result.prob_draw}%`;

        // Role para a seção de resultados e mostre-a
        const resultSection = document.getElementById("result-section");
        resultSection.style.display = "block";
        resultSection.scrollIntoView({ behavior: "smooth" });

    } catch (error) {
        console.error(error);
        alert("Erro ao calcular os resultados. Tente novamente.");
    }
});