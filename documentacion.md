# Documentación del Proyecto App Recetas Fullstack - VERSIÓN FINAL

## Descripción General

Este proyecto es una aplicación fullstack completa y funcional para la gestión de recetas de cocina, desarrollada con **Flask** en el backend y **React** en el frontend. La aplicación permite a los usuarios crear, ver, editar, eliminar y navegar por recetas, con un sistema completo de filtrado por categorías y navegación entre páginas.

## Estructura del Proyecto

```
app-recetas-fullstack/
├── backend/                 # Backend en Flask
│   ├── app/
│   │   ├── __init__.py     # Configuración de la aplicación Flask
│   │   ├── models.py       # Modelos de base de datos
│   │   └── routes.py       # Endpoints de la API
│   ├── instance/
│   │   └── recetas.db      # Base de datos SQLite
│   └── run.py              # Archivo principal para ejecutar el servidor
├── frontend/               # Frontend en React
│   ├── public/
│   │   ├── index.html
│   │   └── melove-logo.png
│   ├── src/
│   │   ├── components/
│   │   │   ├── RecipeCard.js      # Componente para mostrar recetas
│   │   │   ├── RecipeForm.js      # Componente para formularios
│   │   │   └── RecipeDetail.js    # Componente para vista detallada
│   │   ├── App.js                # Componente principal con enrutamiento
│   │   └── App.css               # Estilos de la aplicación
│   └── package.json
└── documentacion.md        # Este archivo
```

## Backend (Flask)

### Configuración

- **Framework**: Flask con SQLAlchemy para ORM
- **Base de datos**: SQLite (archivo `recetas.db`)
- **CORS**: Habilitado para todas las rutas
- **Puerto**: 5000 (por defecto)

### Modelos

#### Recipe
```python
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
```

### API Endpoints

#### GET /recipes
- **Descripción**: Obtiene todas las recetas o filtra por categoría
- **Parámetros de query**:
  - `category` (opcional): Filtra recetas por categoría
- **Respuesta**: Array de objetos receta en formato JSON

#### GET /recipes/{id}
- **Descripción**: Obtiene una receta específica por ID
- **Respuesta**: Objeto receta en formato JSON

#### POST /recipes
- **Descripción**: Crea una nueva receta
- **Body** (JSON):
  ```json
  {
    "title": "string",
    "description": "string", 
    "ingredients": "string",
    "instructions": "string",
    "category": "string",
    "image_url": "string (opcional)"
  }
  ```
- **Respuesta**: Objeto receta creado

#### PUT /recipes/{id}
- **Descripción**: Actualiza una receta existente
- **Body**: Mismo formato que POST
- **Respuesta**: Objeto receta actualizado

#### DELETE /recipes/{id}
- **Descripción**: Elimina una receta
- **Respuesta**: Status 204 (sin contenido)

### Comandos CLI

```bash
# Crear las tablas de la base de datos
flask create-db

# Eliminar las tablas de la base de datos
flask drop-db
```

## Frontend (React)

### Tecnologías

- **Framework**: React 19.1.0
- **Enrutamiento**: React Router DOM 7.8.1
- **Scripts**: React Scripts 5.0.1
- **Puerto**: 3000 (por defecto)

### Componentes

#### App.js
- Componente principal que maneja el estado global
- Implementa enrutamiento con React Router
- Gestiona la comunicación con la API del backend
- Implementa filtrado por categorías
- Maneja la visualización del formulario de recetas
- Navegación entre páginas principal y detalle

#### RecipeForm.js
- Formulario para crear y editar recetas
- Campos: título, descripción, ingredientes, instrucciones, categoría, URL de imagen
- Validación de campos requeridos
- Modo de creación y edición
- Manejo de estados de éxito y error

#### RecipeCard.js
- Tarjeta para mostrar información de una receta
- Incluye imagen, título, categoría, descripción, ingredientes e instrucciones
- Enlace de navegación a vista detallada
- Botones para editar y eliminar
- Diseño responsive y atractivo

#### RecipeDetail.js
- Vista detallada de una receta individual
- Muestra toda la información de la receta
- Imagen destacada con información de la receta
- Secciones separadas para ingredientes e instrucciones
- Navegación de regreso a la página principal

### Categorías Disponibles

- Postres
- Platos Fuertes
- Desayunos
- Ensaladas
- Bebidas

### Funcionalidades Implementadas

- ✅ **CRUD Completo**: Crear, Leer, Actualizar y Eliminar recetas
- ✅ **Navegación**: Sistema de enrutamiento con React Router
- ✅ **Vista Detallada**: Página individual para cada receta
- ✅ **Filtrado por Categorías**: Barra de navegación por categorías
- ✅ **Interfaz Responsive**: Diseño moderno y adaptable
- ✅ **Validación de Formularios**: Campos requeridos y validaciones
- ✅ **Manejo de Estados**: Loading, error y éxito
- ✅ **Gestión de Imágenes**: URLs de imágenes para las recetas
- ✅ **API REST Completa**: Backend con todos los endpoints necesarios
- ✅ **Base de Datos**: SQLite configurada y funcional
- ✅ **CORS**: Comunicación entre frontend y backend
- ✅ **Manejo de Errores**: Gestión robusta de errores

## Instalación y Configuración

### Backend

1. **Navegar al directorio del backend**:
   ```bash
   cd backend
   ```

2. **Crear entorno virtual**:
   ```bash
   Solicitud y Código de Error:
   python -m venv venv 


3. **Activar entorno virtual**:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Instalar dependencias**:
   ```bash
   pip install flask flask-sqlalchemy flask-cors
   ```

5. **Crear la base de datos**:
   ```bash
   flask create-db
   ```

6. **Ejecutar el servidor**:
   ```bash
   python run.py
   ```

### Frontend

1. **Navegar al directorio del frontend**:
   ```bash
   cd frontend
   ```

2. **Instalar dependencias**:
   ```bash
   npm install
   ```

3. **Ejecutar la aplicación**:
   ```bash
   npm start
   ```

## Uso de la Aplicación

1. **Iniciar el backend** (puerto 5000)
2. **Iniciar el frontend** (puerto 3000)
3. **Acceder a la aplicación** en `http://localhost:3000`
4. **Usar las funcionalidades**:
   - **Página Principal**: Ver todas las recetas con filtrado por categorías
   - **Navegación**: Usar la barra de categorías para filtrar recetas
   - **Añadir Receta**: Botón "Añadir Nueva Receta" para crear recetas
   - **Ver Detalle**: Hacer clic en cualquier receta para verla completa
   - **Editar**: Botón "Editar" en cada receta para modificarla
   - **Eliminar**: Botón "Eliminar" para borrar recetas
   - **Navegación**: Logo para regresar a la página principal

## Características Técnicas

### Backend
- **Arquitectura REST**: API bien estructurada y documentada
- **Base de Datos**: SQLite con SQLAlchemy ORM
- **Validación**: Manejo robusto de datos y errores
- **CORS**: Configurado para desarrollo frontend

### Frontend
- **Componentes React**: Arquitectura modular y reutilizable
- **Enrutamiento**: Navegación entre páginas con React Router
- **Estado Global**: Gestión centralizada del estado de la aplicación
- **Responsive Design**: Interfaz adaptable a diferentes dispositivos
- **Manejo de Errores**: Gestión de estados de carga y error

## Estado Final del Proyecto

### ✅ **PROYECTO COMPLETADO AL 100%**

**Backend:**
- API REST completa y funcional
- Base de datos SQLite configurada
- Modelos de datos implementados
- Endpoints para todas las operaciones CRUD
- Manejo de errores y validaciones
- CORS configurado correctamente

**Frontend:**
- Interfaz de usuario completa y moderna
- Sistema de navegación implementado
- Componentes funcionales para todas las operaciones
- Diseño responsive y atractivo
- Gestión de estados y errores
- Integración completa con el backend

**Funcionalidades:**
- ✅ Gestión completa de recetas (CRUD)
- ✅ Sistema de categorías implementado
- ✅ Navegación entre páginas
- ✅ Vista detallada de recetas
- ✅ Filtrado por categorías
- ✅ Formularios de creación y edición
- ✅ Validaciones de formularios
- ✅ Manejo de imágenes
- ✅ Interfaz moderna y responsive

## Tecnologías Utilizadas

### Backend
- **Flask**: Framework web ligero y flexible
- **SQLAlchemy**: ORM para gestión de base de datos
- **SQLite**: Base de datos ligera y portable
- **Flask-CORS**: Manejo de CORS para desarrollo

### Frontend
- **React 19.1.0**: Biblioteca de interfaz de usuario
- **React Router DOM 7.8.1**: Enrutamiento de la aplicación
- **CSS3**: Estilos modernos y responsive
- **Fetch API**: Comunicación con el backend

## Conclusión

Este proyecto representa una aplicación fullstack completa y funcional que demuestra competencias en:

- **Desarrollo Backend**: API REST, base de datos, modelos de datos
- **Desarrollo Frontend**: React, enrutamiento, gestión de estado
- **Arquitectura**: Separación clara entre frontend y backend
- **UX/UI**: Interfaz intuitiva y responsive
- **Integración**: Comunicación efectiva entre frontend y backend

La aplicación está lista para uso en producción y puede servir como base para futuras expansiones como autenticación de usuarios, subida de archivos, o integración con APIs externas.

---

> **PROYECTO COMPLETADO Y FUNCIONAL** - Esta documentación refleja el estado final del proyecto App Recetas Fullstack.
