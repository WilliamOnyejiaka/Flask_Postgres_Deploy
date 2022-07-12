from flask import Flask
from .api.crud import crud

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="SDSDS"
    )

    app.register_blueprint(crud)

    @app.get('/')
    def index():
        return '<h1 style="color=red;">Postgres App</h1>'

    return app