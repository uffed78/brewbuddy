from flask import Flask

def create_app():
    app = Flask(__name__)

    # Konfiguration
    app.config.from_pyfile('config.py', silent=True)

    # Registrera Blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
