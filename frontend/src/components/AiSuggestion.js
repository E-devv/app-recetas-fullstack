import React, { useState } from 'react';
import API_URL from '../config'; // Importamos la configuración

function AiSuggestion({ onSuggestionReceived }) {
  const [ingredients, setIngredients] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGetSuggestion = async () => {
    setLoading(true);
    setError(null);

    try {
      // Usamos API_URL aquí
      const response = await fetch(`${API_URL}/generate-suggestion`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ingredients }),
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.error || `HTTP error! status: ${response.status}`);
      }

      const suggestion = await response.json();
      onSuggestionReceived(suggestion);
    } catch (error) {
      console.error("Error getting AI suggestion:", error);
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ai-suggestion-container">
      <h3>¿Sin inspiración? ¡Prueba nuestro chef con IA!</h3>
      <p>Escribe algunos ingredientes que tengas a mano y deja que la IA te sugiera una receta.</p>
      <div className="ai-suggestion-form">
        <input
          type="text"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          placeholder="Ej: tomate, queso, albahaca"
          disabled={loading}
        />
        <button onClick={handleGetSuggestion} disabled={loading}>
          {loading ? 'Generando...' : 'Obtener Sugerencia'}
        </button>
      </div>
      {error && <p className="submit-status error" style={{marginTop: '10px'}}>{error}</p>}
    </div>
  );
}

export default AiSuggestion;