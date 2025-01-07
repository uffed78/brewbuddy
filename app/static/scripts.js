document.addEventListener("DOMContentLoaded", () => {
    const styleForm = document.getElementById("style-form");
    const chatContainer = document.getElementById("chat-container");
    const chatWindow = document.getElementById("chat-window");
    const recipeContainer = document.getElementById("recipe-container");
    const recipeOutput = document.getElementById("recipe-output");

    // Hämta BJCP-stilar från servern
    fetch("/bjcp-styles")
        .then(response => response.json())
        .then(styles => {
            const styleSelect = document.getElementById("bjcp-style");
            styles.forEach(style => {
                const option = document.createElement("option");
                option.value = style.name;
                option.textContent = `${style.name} - ${style.description}`;
                styleSelect.appendChild(option);
            });
        });

    // Starta chatten
    document.getElementById("load-chat").addEventListener("click", () => {
        styleForm.style.display = "none";
        chatContainer.style.display = "block";
        const selectedStyle = document.getElementById("bjcp-style").value;
        chatWindow.innerHTML += `<div class="bot-message">You selected: ${selectedStyle}</div>`;
    });

    // Skicka meddelande till ChatGPT
    document.getElementById("send-message").addEventListener("click", () => {
        const userInput = document.getElementById("user-input").value;
        chatWindow.innerHTML += `<div class="user-message">${userInput}</div>`;
        fetch("/generate-recipe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_input: userInput })
        })
            .then(response => response.json())
            .then(data => {
                chatWindow.innerHTML += `<div class="bot-message">${data.response}</div>`;
            });
    });

    async function loadInventory() {
        const response = await fetch('/api/brewfather/inventory');
        const inventory = await response.json();
        displayInventory(inventory);
    }
    
    function displayInventory(inventory) {
        const inventoryDiv = document.getElementById('inventory');
        inventoryDiv.innerHTML = inventory.map(item => `
            <label>
                <input type="checkbox" value="${item.name}">
                ${item.name}
            </label>
        `).join('');
    }
    
    document.getElementById('recipe-form').addEventListener('submit', async (event) => {
        event.preventDefault();
    
        const beerStyle = document.getElementById('beer-style').value;
        const selectedIngredients = Array.from(document.querySelectorAll('#inventory input:checked'))
            .map(input => input.value);
    
        const response = await fetch('/api/generate-recipe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ beer_style: beerStyle, selected_ingredients: selectedIngredients }),
        });
    
        const data = await response.json();
        const recipeResult = document.getElementById('recipe-result');
        recipeResult.innerText = data.recipe || data.error;
    });

    
    
    // Generera recept
    document.getElementById("generate-recipe").addEventListener("click", () => {
        fetch("/generate-recipe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ finalize: true })
        })
            .then(response => response.json())
            .then(data => {
                chatContainer.style.display = "none";
                recipeContainer.style.display = "block";
                recipeOutput.textContent = data.recipe;
            });
    });
});
