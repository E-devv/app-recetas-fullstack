from app import create_app, db

app = create_app()

@app.cli.command("create-db")
def create_db():
    """Crea las tablas de la base de datos."""
    with app.app_context():
        db.create_all()
    print("Base de datos creada!")

@app.cli.command("drop-db")
def drop_db():
    """Elimina las tablas de la base de datos."""
    with app.app_context():
        db.drop_all()
    print("Base de datos eliminada!")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)