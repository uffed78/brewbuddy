import json
import os

def load_beer_styles():
    """
    Läser in bjcp_styles.json och returnerar en lista med ölstilar.
    :return: Lista med ölstilsdata.
    """
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'bjcp_styles.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            beer_styles = json.load(file)
        return beer_styles
    except FileNotFoundError:
        print("Filen bjcp_styles.json kunde inte hittas.")
        return []
    except json.JSONDecodeError:
        print("Det uppstod ett fel vid läsning av bjcp_styles.json.")
        return []

def search_beer_styles(beer_styles, search_term):
    """
    Sök efter ölstilar baserat på namn eller kategori.
    :param beer_styles: Lista med ölstilar.
    :param search_term: Sökterm som användaren anger.
    :return: Lista med ölstilar som matchar sökningen.
    """
    results = [
        style for style in beer_styles
        if search_term.lower() in style['name'].lower() or search_term.lower() in style.get('category', '').lower()
    ]
    return results

def filter_beer_styles_by_ingredients(beer_styles, available_ingredients):
    """
    Filtrera ölstilar baserat på användarens tillgängliga ingredienser.
    :param beer_styles: Lista med ölstilar.
    :param available_ingredients: Mängd med användarens tillgängliga ingredienser (lowercased).
    :return: Lista med ölstilar som matchar de tillgängliga ingredienserna.
    """
    matching_styles = []
    for style in beer_styles:
        required_ingredients = set(style.get('ingredients', []))
        if required_ingredients.issubset(available_ingredients):
            matching_styles.append(style)
    return matching_styles
