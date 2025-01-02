from flask import Flask
from flask_dotenv import DotEnv

def create_app():
    app = Flask(__name__)
    env = DotEnv(app)
    env.init_app(app, env_file=".env")

    from app.routes import main
    app.register_blueprint(main)

    return app
