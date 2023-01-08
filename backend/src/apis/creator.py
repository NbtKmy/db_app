from flask_restful import Resource, reqparse, abort
from flask import jsonify
from src.models.creator import CreatorModel, CreatorSchema
from src.database import db

class CreatorAllAPI(Resource):

    def get(self):
    results = CreatorModel.query.all()
    jsonData = CreatorSchema(many=True).dump(results).data
    return jsonify({'items': jsonData})


class CreatorAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type = str, location='args')
    parser.add_argument('name_ja', type = str, location='args')
    parser.add_argument('name_en', type = str, location='args')
    altnames = request.args.get('altnames', type = str, location='args')

    def get(self):
        args = parser.parse_args()

        creator = db.session.query(CreatorModel).filter_by(id=id).first()
        if creator is None:
            abort(404)

        res = CreatorSchema().dump(creator).data
        return res


