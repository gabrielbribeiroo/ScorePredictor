document.getElementById("match-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const homeTeam = document.getElementById("home-team").value;
    const awayTeam = document.getElementById("away-team").value;
    const homeDesfalque = document.getElementById("home-desfalque").value;
    const awayDesfalque = document.getElementById("away-desfalque").value;

    // Fazer a solicitação para o servidor
    const response = await fetch("/api/prever_resultado", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            homeTeam,
            awayTeam,
            homeDesfalque,
            awayDesfalque,
        }),
    });

    const result = await response.json();

    // Atualizar os resultados na interface
    document.getElementById("home-prob").innerText = `Probabilidade de ${homeTeam} ganhar: ${result.ProbCasa.toFixed(2)}%`;
    document.getElementById("away-prob").innerText = `Probabilidade de ${awayTeam} ganhar: ${result.ProbFora.toFixed(2)}%`;
    document.getElementById("draw-prob").innerText = `Probabilidade de empate: ${result.ProbEmpate.toFixed(2)}%`;

    // Rolar automaticamente para a seção de resultados
    document.getElementById("result").scrollIntoView({ behavior: "smooth" });
});
