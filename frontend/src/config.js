// frontend/src/config.js
const API_URL = process.env.NODE_ENV === 'production'
  ? 'https://app-recetas-backend.onrender.com' // ⚠️ CAMBIAREMOS ESTO LUEGO CON TU URL REAL
  : 'http://localhost:5000';

export default API_URL;