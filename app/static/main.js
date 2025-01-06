// Funktion för att söka efter ölstilar
async function searchStyles() {
    const searchTerm = document.getElementById('search-term').value;
    const resultsDiv = document.getElementById('search-results');
    resultsDiv.innerHTML = 'Laddar...';

    try {
        const response = await fetch(`/api/styles/search?term=${encodeURIComponent(searchTerm)}`);
        const data = await response.json();

        if (response.ok) {
            resultsDiv.innerHTML = `<h3>Resultat:</h3><ul>${data.map(style => `<li>${style.name}</li>`).join('')}</ul>`;
        } else {
            resultsDiv.innerHTML = `<p>Fel: ${data.error || 'Något gick fel'}</p>`;
        }
    } catch (error) {
        resultsDiv.innerHTML = `<p>Fel: ${error.message}</p>`;
    }
}

// Funktion för att filtrera ölstilar baserat på ingredienser
async function filterStyles() {
    const ingredientsInput = document.getElementById('ingredients').value;
    const ingredients = ingredientsInput.split(',').map(ing => ing.trim());
    const resultsDiv = document.getElementById('filter-results');
    resultsDiv.innerHTML = 'Laddar...';

    try {
        const response = await fetch('/api/styles/filter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ingredients }),
        });

        const data = await response.json();

        if (response.ok) {
            resultsDiv.innerHTML = `<h3>Resultat:</h3><ul>${data.map(style => `<li>${style.name} (${style.category})</li>`).join('')}</ul>`;
        } else {
            resultsDiv.innerHTML = `<p>Fel: ${data.error || 'Något gick fel'}</p>`;
        }
    } catch (error) {
        resultsDiv.innerHTML = `<p>Fel: ${error.message}</p>`;
    }
}
