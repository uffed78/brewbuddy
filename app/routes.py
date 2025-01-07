from flask import Blueprint, jsonify, request, render_template
from app.utils.brewfather import fetch_inventory, fetch_recipes
from app.utils.openai_integration import generate_recipe, handle_chat
from app.models import db, Recipe

# Definiera Blueprint
main = Blueprint('main', __name__)

# API-routes för Brewfather
@main.route('/brewfather/inventory')
def get_inventory():
    """Hämta användarens inventory från Brewfather."""
    return jsonify(fetch_inventory())

@main.route('/brewfather/recipes')
def get_recipes():
    """Hämta användarens recept från Brewfather."""
    return jsonify(fetch_recipes())

# Route för BJCP-stilar
@main.route('/bjcp-styles')
def get_bjcp_styles():
    """Hämta BJCP-stilar."""
    return jsonify(fetch_bjcp_styles())

# Route för ChatGPT-receptgenerering
@main.route('/generate-recipe', methods=['POST'])
def generate_recipe_endpoint():
    """Hantera receptgenerering via ChatGPT."""
    data = request.json
    if data.get("finalize"):
        # Generera slutgiltigt recept
        return jsonify({"recipe": generate_recipe(data["bjcp_style"], data["inventory"])})
    else:
        # Hantera användarchatt
        response = handle_chat(data.get("user_input"))
        return jsonify({"response": response})

# Frontend-route
@main.route('/', methods=['GET', 'POST'])
def home():
    """Frontend för BrewBuddy."""
    recipe = None
    if request.method == 'POST':
        bjcp_style = {
            "name": request.form.get('name'),
            "description": request.form.get('description')
        }
        inventory = {
            "fermentables": [{"name": f.strip()} for f in request.form.get('fermentables').split(',')],
            "hops": [{"name": h.strip()} for h in request.form.get('hops').split(',')],
            "yeasts": [{"name": y.strip()} for y in request.form.get('yeasts').split(',')]
        }
        recipe = generate_recipe(bjcp_style, inventory)

    return render_template('index.html', recipe=recipe)

@main.route('/save-recipe', methods=['POST'])
def save_recipe():
    """Spara ett genererat recept i databasen."""
    data = request.json
    name = data.get("name")
    bjcp_style = data.get("bjcp_style")
    inventory = data.get("inventory")
    generated_recipe = data.get("generated_recipe")

    if not all([name, bjcp_style, inventory, generated_recipe]):
        return jsonify({"error": "Alla fält är obligatoriska"}), 400

    new_recipe = Recipe(
        name=name,
        bjcp_style=bjcp_style,
        inventory=inventory,
        generated_recipe=generated_recipe
    )
    db.session.add(new_recipe)
    db.session.commit()

    return jsonify({"message": "Recept sparat", "recipe_id": new_recipe.id}), 201

@main.route('/saved-recipes', methods=['GET'])
def saved_recipes():
    """Lista alla sparade recept."""
    recipes = Recipe.query.order_by(Recipe.timestamp.desc()).all()
    return jsonify([recipe.to_dict() for recipe in recipes])

@main.route('/recipe/<int:id>', methods=['GET'])
def get_recipe(id):
    """Hämta ett specifikt recept baserat på ID."""
    recipe = Recipe.query.get_or_404(id)
    return jsonify(recipe.to_dict())