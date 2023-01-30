from flask_restful import Resource, reqparse, abort
from flask import jsonify
from src.models.databaselist import DatabaselistModel, DatabaselistSchema



class DatabaselistAllAPI(Resource):


    def get(self):
        results = DatabaselistModel.query.all()
        return jsonify({'databaselist': DatabaselistSchema(many=True).dump(results)})


class DatabaselistAPI(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, default='*', location='args')
        parser.add_argument('titel_ja', type=str, location='args')
        parser.add_argument('titel_en', type=str, location='args')
        parser.add_argument('creator_id', type=str, location='args')
        parser.add_argument('ddc_category', type=str, location='args')
        parser.add_argument('type', type=str, location='args')
        parser.add_argument('description_ja', type=str, location='args')
        parser.add_argument('description_en', type=str, location='args')

        parser.add_argument('page', type=int, default=1)
        parser.add_argument('per_page', type=int, default=20)

        args = parser.parse_args()

        page = args.page
        per_page = args.per_page

        args_without_page = args.pop('page')
        kwds = args_without_page.pop('per_page')

        results = DatabaselistModel.query().filter_by(**kwds).order_by(DatabaselistModel.id).all()
        if results is None:
            abort(404)

        return jsonify({
            'page': page,
            'per_page': per_page,
            'has_next': results.has_next,
            'has_prev': results.has_prev,
            'page_list': [iter_page if iter_page else '...' for iter_page in results.iter_pages()],
            'databases': DatabaselistSchema(many=True).dump(results)})