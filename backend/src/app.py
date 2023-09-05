from flask import Flask
from flask_restful import Api
from database import init_db
from src.apis import creator
from src.apis import databaselist
#from .apis.creator import CreatorAllAPI, CreatorAPI
#from .apis.databaselist import DatabaselistAllAPI, DatabaselistAPI
from flask_cors import CORS


def create_app():

    

    app = Flask(__name__)
    CORS(app)
    app.config.from_object('src.config.Config')

    init_db()

    api = Api(app)
    api.add_resource(creator.CreatorAllAPI, '/creator/all')
    api.add_resource(creator.CreatorAPI, '/creator/search')
    api.add_resource(databaselist.DatabaselistAllAPI, '/databaselist/all')
    api.add_resource(databaselist.DatabaselistAPI, '/databaselist/search')

    return app


app = create_app()
