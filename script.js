document.addEventListener("DOMContentLoaded", async function () {
    async function fetchData(url, elementId) {
        try {
            let response = await fetch(url);
            let data = await response.json();
            document.getElementById(elementId).innerHTML = JSON.stringify(data, null, 2);
        } catch (error) {
            document.getElementById(elementId).innerHTML = "Error fetching data!";
        }
    }

    fetchData("cricket.json", "cricket");
    fetchData("football.json", "football");
});
