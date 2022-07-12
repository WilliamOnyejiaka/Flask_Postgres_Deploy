from flask import Flask
from .api.crud import crud
from .config import HOST,PASSWORD,DBNAME,PORT,USER

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="SDSDS"
    )

    app.register_blueprint(crud)

    @app.get('/')
    def index():
        return '<h1 style="color=red;">Postgres App</h1>'

    @app.get('/config')
    def con():
        return [HOST,PASSWORD,DBNAME,PORT,USER]
    return app