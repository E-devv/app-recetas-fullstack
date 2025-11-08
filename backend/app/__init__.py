import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app) # Habilitar CORS para todas las rutas

    # Configuración de la base de datos
    # Intenta obtener la URL de la base de datos desde las variables de entorno (Render la proporciona automáticamente)
    # Si no existe (como en tu PC local), usa SQLite por defecto.
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///recetas.db')

    # Pequeño arreglo necesario para algunas versiones de SQLAlchemy en Render
    # que a veces entrega URLs que empiezan con 'postgres://' en lugar de 'postgresql://'
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Importar y registrar blueprints (rutas)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app