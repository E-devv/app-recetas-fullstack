import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import '../App.css';
import API_URL from '../config'; // Importamos la configuración

function RecipeDetail() {
    const { id } = useParams();
    const [recipe, setRecipe] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecipe = async () => {
            try {
                // Usamos API_URL aquí
                const response = await fetch(`${API_URL}/recipes/${id}`);
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                setRecipe(data);
            } catch (error) {
                console.error("Error fetching recipe:", error);
                setError("No se pudo cargar la receta. Asegúrate de que el backend está corriendo.");
            } finally {
                setLoading(false);
            }
        };

        fetchRecipe();
    }, [id]);

    if (loading) return <p>Cargando receta...</p>;
    if (error) return <p className="submit-status error">{error}</p>;
    if (!recipe) return <p>Receta no encontrada.</p>;

    return (
        <div className="recipe-detail-container">
            <div className="recipe-detail-header">
                <img src={recipe.image_url} alt={recipe.title} className="recipe-detail-image" />
                <div className="recipe-detail-info">
                    <h1>{recipe.title}</h1>
                    <p className="recipe-detail-description">{recipe.description}</p>
                    <p className="recipe-detail-category">Categoría: <strong>{recipe.category}</strong></p>
                </div>
            </div>
            <div className="recipe-detail-content">
                <div className="ingredients-section">
                    <h2>Ingredientes</h2>
                    <p>{recipe.ingredients}</p>
                </div>
                <div className="instructions-section">
                    <h2>Instrucciones</h2>
                    <p>{recipe.instructions}</p>
                </div>
            </div>
        </div>
    );
}

export default RecipeDetail;