from flask_restful import Resource, reqparse, abort
from flask import jsonify
from src.models.creator import CreatorModel, CreatorSchema
from src.database import db

class CreatorAllAPI(Resource):

    def get(self):
        results = CreatorModel.query.all()
        return jsonify({'creators': CreatorSchema(many=true, exclude=('geo')).dump(results).data})


class CreatorAPI(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type = str, location='args')
        parser.add_argument('name_ja', type = str, location='args')
        parser.add_argument('name_en', type = str, location='args')
        parser.add_argument('altnames', type = str, location='args')
        args = parser.parse_args()

        results = db.session.query(CreatorModel).filter_by(**args).all()
        if results is None:
            abort(404)

        return jsonify({'creators': CreatorSchema(many=true, exclude=('geo')).dump(results).data})


