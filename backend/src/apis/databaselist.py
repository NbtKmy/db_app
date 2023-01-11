from flask_restful import Resource, reqparse, abort
from flask import jsonify
from src.models.databaselist import DatabaselistModel, DatabaselistSchema
from src.database import db

class DatabaselistAllAPI(Resource):

    def get(self):
        results = DatabaselistModel.query.all()
        return jsonify({'databaselist': DatabaselistSchema(many=true).dump(results).data})


class DatabaselistAPI(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type = str, location='args')
        parser.add_argument('titel_ja', type = str, location='args')
        parser.add_argument('titel_en', type = str, location='args')
        parser.add_argument('creator_id', type = str, location='args')
        parser.add_argument('ddc_category', type = str, location='args')
        parser.add_argument('type', type = str, location='args')
        parser.add_argument('description_ja', type = str, location='args')
        parser.add_argument('description_en', type = str, location='args')

        args = parser.parse_args()

        results = db.session.query(DatabaselistModel).filter_by(**args).all()
        if results is None:
            abort(404)

        return jsonify({'creators': DatabaselistSchema(many=true).dump(results).data})
