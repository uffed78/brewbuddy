import sys
import os

# Lägg till sökvägen till utils i sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app', 'utils'))

from beer_styles import load_beer_styles, search_beer_styles
from beer_styles import filter_beer_styles_by_ingredients

def test_search_beer_styles():
    beer_styles = load_beer_styles()
    if not beer_styles:
        print("Inga ölstilar att söka i.")
        return

    search_term = input("Ange sökterm (namn eller kategori): ").strip()
    results = search_beer_styles(beer_styles, search_term)

    if results:
        print(f"\nHittade {len(results)} ölstilar som matchar '{search_term}':")
        for style in results:
            print(f"- {style['name']} (Kategori: {style.get('category', 'Ingen kategori')})")
    else:
        print(f"\nInga ölstilar matchar '{search_term}'.")

if __name__ == "__main__":
    test_search_beer_styles()


def test_load_beer_styles():
    beer_styles = load_beer_styles()
    if beer_styles:
        print(f"Laddade in {len(beer_styles)} ölstilar.")
        # Visa de tre första ölstilarna som exempel
        for style in beer_styles[:3]:
            print(f"- {style['name']}")
    else:
        print("Inga ölstilar kunde laddas.")

if __name__ == "__main__":
    test_load_beer_styles()


def test_filter_beer_styles():
    beer_styles = load_beer_styles()
    if not beer_styles:
        print("Inga ölstilar att filtrera.")
        return

    # Simulerade ingredienser från användaren
    available_ingredients = input("Ange dina ingredienser, separerade med kommatecken: ").strip().lower().split(",")
    available_ingredients = {ingredient.strip() for ingredient in available_ingredients}

    matching_styles = filter_beer_styles_by_ingredients(beer_styles, available_ingredients)

    if matching_styles:
        print(f"\nFöljande {len(matching_styles)} ölstilar kan skapas med dina ingredienser:")
        for style in matching_styles:
            print(f"- {style['name']} (Ingredienser: {', '.join(style.get('ingredients', []))})")
    else:
        print("\nInga ölstilar matchar dina ingredienser.")

if __name__ == "__main__":
    test_filter_beer_styles()
