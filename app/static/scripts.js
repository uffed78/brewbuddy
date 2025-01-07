document.addEventListener("DOMContentLoaded", () => {
    // Ladda BJCP-stilar från backend
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

    // Hantera klick för att starta chatten
    document.getElementById("load-chat").addEventListener("click", () => {
        document.getElementById("style-form").style.display = "none";
        document.getElementById("chat-container").style.display = "block";
        const selectedStyle = document.getElementById("bjcp-style").value;
        document.getElementById("chat-window").innerHTML += `<div class="bot-message">You selected: ${selectedStyle}</div>`;
    });

    // Skicka meddelande till ChatGPT
    document.getElementById("send-message").addEventListener("click", () => {
        const userInput = document.getElementById("user-input").value;
        const chatWindow = document.getElementById("chat-window");
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

    // Spara recept
    document.getElementById("save-recipe").addEventListener("click", () => {
        const recipeName = prompt("Enter a name for the recipe:");
        const bjcpStyle = document.getElementById("bjcp-style").value;
        const inventory = JSON.stringify({ /* Du kan fylla med aktuellt inventory */ });
        const generatedRecipe = document.getElementById("recipe-output").textContent;

        fetch("/save-recipe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: recipeName,
                bjcp_style: bjcpStyle,
                inventory: inventory,
                generated_recipe: generatedRecipe
            })
        })
            .then(response => response.json())
            .then(data => {
                alert("Recipe saved!");
                loadSavedRecipes();
            });
    });

    // Ladda sparade recept
    function loadSavedRecipes() {
        fetch("/saved-recipes")
            .then(response => response.json())
            .then(recipes => {
                const list = document.getElementById("saved-recipes-list");
                list.innerHTML = "";
                recipes.forEach(recipe => {
                    const listItem = document.createElement("li");
                    listItem.textContent = `${recipe.name} (${recipe.bjcp_style})`;
                    list.appendChild(listItem);
                });
                document.getElementById("saved-recipes-container").style.display = "block";
            });
    }
});
