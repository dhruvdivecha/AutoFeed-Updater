document.addEventListener("DOMContentLoaded", () => {
    const cricketAPI = "https://api.example.com/cricket"; // Replace with actual API endpoint
    const footballAPI = "https://v3.football.api-sports.io/e527606df5ab264030b3dd901fcf05c7"

    async function fetchData(url, elementId) {
        try {
            const response = await fetch(url);
            const data = await response.json();
            const container = document.getElementById(elementId);
            container.innerHTML = ""; // Clear existing content

            data.matches.forEach(match => {
                const div = document.createElement("div");
                div.innerHTML = `
                    <h3>${match.team1.name} vs ${match.team2.name}</h3>
                    <p><strong>Date:</strong> ${match.date} | <strong>Time:</strong> ${match.time}</p>
                    <p><strong>Venue:</strong> ${match.venue}</p>
                    <p><strong>Status:</strong> ${match.status}</p>
                `;
                container.appendChild(div);
            });
        } catch (error) {
            document.getElementById(elementId).innerHTML = "Error fetching data!";
        }
    }

    fetchData(cricketAPI, "cricket");
    fetchData(footballAPI, "football");
});
