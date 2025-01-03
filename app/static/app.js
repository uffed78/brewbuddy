// Funktion för att hämta och visa fermentables
async function fetchFermentables() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/inventory/fermentables");
        const data = await response.json();
        const list = document.getElementById("fermentables-list");
        data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.name} (${item.amount}g)`;
            list.appendChild(li);
        });
    } catch (error) {
        console.error("Error fetching fermentables:", error);
    }
}

// Funktion för att hämta och visa hops
async function fetchHops() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/inventory/hops");
        const data = await response.json();
        const list = document.getElementById("hops-list");
        data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.name} (${item.alpha}%)`;
            list.appendChild(li);
        });
    } catch (error) {
        console.error("Error fetching hops:", error);
    }
}

// Funktion för att hämta och visa yeasts
async function fetchYeasts() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/inventory/yeasts");
        const data = await response.json();
        const list = document.getElementById("yeasts-list");
        data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `${item.name} (${item.attenuation}%)`;
            list.appendChild(li);
        });
    } catch (error) {
        console.error("Error fetching yeasts:", error);
    }
}

// Kör alla fetch-funktioner vid sidladdning
fetchFermentables();
fetchHops();
fetchYeasts();
