from flask import Flask
from flask_restful import Api
from .database import init_db
from .apis.creator import CreatorAllAPI, CreatorAPI
from .apis.databaselist import DatabaselistAllAPI, DatabaselistAPI
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    CORS(app)
    app.config.from_object('src.config.Config')

    init_db()

    api = Api(app)
    api.add_resource(CreatorAllAPI, '/creator/all')
    api.add_resource(CreatorAPI, '/creator/search')
    api.add_resource(DatabaselistAllAPI, '/databaselist/all')
    api.add_resource(DatabaselistAPI, '/databaselist/search')

    return app


app = create_app()
