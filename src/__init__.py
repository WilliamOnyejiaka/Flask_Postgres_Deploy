from flask import Flask
from .api.crud import crud

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="SDSDS"
    )

    app.register_blueprint(crud)

    return app