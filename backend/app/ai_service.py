import time
import random

def get_ai_suggestion(ingredients):
    """
    Simulates a call to an AI service to get a recipe suggestion.
    In a real application, this would involve a network request to an AI API.
    """
    # Simulate network latency
    time.sleep(2)

    # Simulate potential errors from the AI service
    if "error" in ingredients.lower():
        raise Exception("AI service failed to generate a suggestion.")

    # Simulate empty or incomplete response
    if "empty" in ingredients.lower():
        return None

    # Simulate a successful response
    suggestions = [
        {
            "title": "Ensalada Fresca de Verano",
            "description": "Una ensalada ligera y refrescante, perfecta para un día caluroso.",
            "instructions": "1. Lava y corta las verduras. 2. Mezcla todos los ingredientes en un bol grande. 3. Aliña con aceite de oliva, sal y pimienta al gusto."
        },
        {
            "title": "Sopa de Tomate Casera",
            "description": "Una sopa reconfortante y llena de sabor, ideal para una cena ligera.",
            "instructions": "1. Sofríe la cebolla y el ajo. 2. Añade los tomates y el caldo. 3. Cocina a fuego lento durante 20 minutos y luego tritura."
        },
        {
            "title": "Tacos de Pollo Rápidos",
            "description": "Una opción rápida y deliciosa para cualquier día de la semana.",
            "instructions": "1. Cocina el pollo con tus especias favoritas. 2. Calienta las tortillas. 3. Rellena los tacos con el pollo y tus toppings preferidos."
        }
    ]

    suggestion = random.choice(suggestions)

    return {
        "title": suggestion["title"],
        "description": suggestion["description"],
        "instructions": suggestion["instructions"]
    }