document.addEventListener("DOMContentLoaded", () => {
    const apiKey = "e527606df5ab264030b3dd901fcf05c7"
    const apiUrl = " https://v3.football.api-sports.io";

    async function fetchFootballData() {
        try {
            const response = await fetch(apiUrl, {
                headers: { "X-Auth-Token": apiKey }
            });
            const data = await response.json();
            const container = document.getElementById("football");
            container.innerHTML = ""; // Clear existing content

            data.matches.forEach(match => {
                const div = document.createElement("div");
                div.innerHTML = `
                    <h3>${match.homeTeam.name} vs ${match.awayTeam.name}</h3>
                    <p><strong>Competition:</strong> ${match.competition.name}</p>
                    <p><strong>Date:</strong> ${new Date(match.utcDate).toLocaleString()}</p>
                    <p><strong>Status:</strong> ${match.status}</p>
                    <p><strong>Score:</strong> ${match.score.fullTime.homeTeam} - ${match.score.fullTime.awayTeam}</p>
                `;
                container.appendChild(div);
            });
        } catch (error) {
            document.getElementById("football").innerHTML = "Error fetching football data.";
            console.error(error);
        }
    }

    fetchFootballData();
});
