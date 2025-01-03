from flask import Blueprint, jsonify, request
from app.utils.brewfather import fetch_inventory, fetch_recipes, fetch_specific_inventory
from app.utils.bjcp import fetch_bjcp_styles
from app.utils.openai_integration import generate_recipe

# Definiera Blueprint
main = Blueprint('main', __name__)

@main.route('/brewfather/inventory')
def get_inventory():
    """
    Hämtar hela inventariet från Brewfather.
    """
    return jsonify(fetch_inventory())

@main.route('/brewfather/inventory/fermentables')
def get_fermentables():
    """
    Hämtar malt (fermentables) från Brewfather-inventory.
    """
    return jsonify(fetch_specific_inventory("fermentables"))

@main.route('/brewfather/inventory/hops')
def get_hops():
    """
    Hämtar humle (hops) från Brewfather-inventory.
    """
    return jsonify(fetch_specific_inventory("hops"))

@main.route('/brewfather/inventory/yeasts')
def get_yeasts():
    """
    Hämtar jäst (yeasts) från Brewfather-inventory.
    """
    return jsonify(fetch_specific_inventory("yeasts"))

@main.route('/brewfather/recipes')
def get_recipes():
    """
    Hämtar recept från Brewfather.
    """
    return jsonify(fetch_recipes())

@main.route('/bjcp-styles')
def get_bjcp_styles():
    """
    Hämtar BJCP-stilar från BJCP-guiden.
    """
    return jsonify(fetch_bjcp_styles())

@main.route('/generate-recipe', methods=['POST'])
def generate_recipe_endpoint():
    """
    Hanterar GPT-baserat receptskapande.
    """
    data = request.json
    context = data.get("context")  # Exempel: "inventory", "recipe", "bjcp"
    user_input = data.get("user_input")  # Data baserat på användarens val
    recipe = generate_recipe(context, user_input)
    return jsonify({"recipe": recipe})
