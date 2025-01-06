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
