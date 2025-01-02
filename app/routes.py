from flask import Blueprint, jsonify, request
from app.utils.brewfather import fetch_inventory, fetch_recipes
from app.utils.bjcp import fetch_bjcp_styles
from app.utils.openai_integration import generate_recipe

# Definiera Blueprint
main = Blueprint('main', __name__)

@main.route('/brewfather/inventory')
def get_inventory():
    return jsonify(fetch_inventory())

@main.route('/brewfather/recipes')
def get_recipes():
    return jsonify(fetch_recipes())

@main.route('/bjcp-styles')
def get_bjcp_styles():
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
