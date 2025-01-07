from flask import Blueprint, jsonify, request
from flask import Blueprint, render_template, request
from .utils.brewfather import fetch_inventory, fetch_recipes, fetch_specific_inventory
from .utils.bjcp import fetch_bjcp_styles
from .utils.openai_integration import generate_recipe, suggest_beer_styles
from app.utils.brewfather import fetch_inventory, fetch_recipes, fetch_specific_inventory
from app.utils.bjcp import fetch_bjcp_styles
from app.utils.openai_integration import generate_recipe, suggest_beer_styles




# Definiera Blueprint
main = Blueprint('main', __name__)

@main.route('/api')
def index():
    return jsonify({"message": "Välkommen till BrewBuddy API!"})

@main.route('/brewfather/inventory')
def get_inventory():
    return jsonify(fetch_inventory())

@main.route('/brewfather/inventory/fermentables')
def get_fermentables():
    return jsonify(fetch_specific_inventory("fermentables"))

@main.route('/brewfather/inventory/hops')
def get_hops():
    return jsonify(fetch_specific_inventory("hops"))

@main.route('/brewfather/inventory/yeasts')
def get_yeasts():
    return jsonify(fetch_specific_inventory("yeasts"))

@main.route('/brewfather/recipes')
def get_recipes():
    return jsonify(fetch_recipes())

@main.route('/bjcp-styles')
def get_bjcp_styles():
    return jsonify(fetch_bjcp_styles())

@main.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    """
    Använd ChatGPT för att generera ett ölrecept baserat på användarens val.
    """
    data = request.get_json()
    selected_ingredients = data.get('selected_ingredients', [])
    beer_style = data.get('beer_style', 'Pale Ale')

    if not selected_ingredients:
        return jsonify({"error": "Inga ingredienser valda"}), 400

    try:
        recipe = generate_recipe_with_gpt(beer_style, selected_ingredients)
        return jsonify({"recipe": recipe}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@main.route('/', methods=['GET', 'POST'])
def home():
    recipe = None
    if request.method == 'POST':
        # Hämta data från formuläret
        bjcp_style = {
            "name": request.form.get('name'),
            "description": request.form.get('description')
        }
        inventory = {
            "fermentables": [{"name": f.strip()} for f in request.form.get('fermentables').split(',')],
            "hops": [{"name": h.strip()} for h in request.form.get('hops').split(',')],
            "yeasts": [{"name": y.strip()} for y in request.form.get('yeasts').split(',')]
        }

        # Generera recept
        recipe = generate_recipe(bjcp_style, inventory)

    return render_template('index.html', recipe=recipe)

@main.route('/suggest_styles', methods=['POST'])
def suggest_styles():
    """
    Använd OpenAI för att föreslå ölstilar baserat på användarens ingredienser.
    """
    data = request.get_json()
    ingredients = data.get('ingredients', [])

    if not ingredients:
        return jsonify({"error": "Inga ingredienser angivna"}), 400

    # Använd funktionen från openai_integration.py
    suggestions = suggest_beer_styles(ingredients)
    return jsonify({"suggestions": suggestions}), 200
