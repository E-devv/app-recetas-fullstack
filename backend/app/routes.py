from flask import Blueprint, request, jsonify
from app import db
from app.models import Recipe
from app.ai_service import get_ai_suggestion

main = Blueprint('main', __name__)

@main.route('/recipes', methods=['GET'])
def get_recipes():
    # Obtener el parámetro 'category' de la URL si existe
    category = request.args.get('category')

    if category:
        # Si se proporciona una categoría, filtra las recetas por esa categoría
        recipes = Recipe.query.filter_by(category=category).all()
    else:
        # Si no se proporciona categoría, devuelve todas las recetas
        recipes = Recipe.query.all()

    recipes_data = [{
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'category': recipe.category,
        'image_url': recipe.image_url
    } for recipe in recipes]
    return jsonify(recipes_data)

@main.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe.to_dict())

@main.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.json
    # Validación de campos requeridos
    required_fields = ['title', 'description', 'ingredients', 'instructions']
    if not all(field in data and data[field] for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    new_recipe = Recipe(
        title=data['title'],
        description=data['description'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        category=data.get('category', 'General'),
        image_url=data.get('image_url')
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify(new_recipe.to_dict()), 201

@main.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.json

    # Validación de campos requeridos
    if 'title' in data and not data['title']:
        return jsonify({"error": "Title cannot be empty"}), 400
    if 'description' in data and not data['description']:
        return jsonify({"error": "Description cannot be empty"}), 400
    if 'ingredients' in data and not data['ingredients']:
        return jsonify({"error": "Ingredients cannot be empty"}), 400
    if 'instructions' in data and not data['instructions']:
        return jsonify({"error": "Instructions cannot be empty"}), 400

    recipe.title = data.get('title', recipe.title)
    recipe.description = data.get('description', recipe.description)
    recipe.ingredients = data.get('ingredients', recipe.ingredients)
    recipe.instructions = data.get('instructions', recipe.instructions)
    recipe.category = data.get('category', recipe.category)
    recipe.image_url = data.get('image_url', recipe.image_url)
    db.session.commit()
    return jsonify(recipe.to_dict())

@main.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return '', 204

@main.route('/generate-suggestion', methods=['POST'])
def generate_suggestion():
    data = request.json
    ingredients = data.get('ingredients')

    if not ingredients:
        return jsonify({"error": "Ingredients are required"}), 400

    try:
        suggestion = get_ai_suggestion(ingredients)
        if suggestion is None:
            return jsonify({"error": "AI service returned an empty response"}), 500

        # Basic prompt injection mitigation
        if any(keyword in ingredients.lower() for keyword in ["ignore", "instruction", "prompt"]):
             return jsonify({"error": "Invalid input detected"}), 400

        return jsonify(suggestion)
    except Exception as e:
        # Log the error for debugging
        print(f"Error calling AI service: {e}")
        return jsonify({"error": "Failed to get suggestion from AI service"}), 500