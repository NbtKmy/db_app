from flask_restful import Resource, reqparse, abort
from flask import jsonify
from src.models.creator import CreatorModel, CreatorSchema


class CreatorAllAPI(Resource):

    def get(self):
        results = CreatorModel.query.all()
        return jsonify({'creators': CreatorSchema(many=True, exclude=['geo']).dump(results)})


class CreatorAPI(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type = str, default = '*', location='args')
        parser.add_argument('name_ja', type = str, location='args')
        parser.add_argument('name_en', type = str, location='args')
        parser.add_argument('altnames', type = str, location='args')
        parser.add_argument('page', type = int, default = 1)
        parser.add_argument('per_page', type = int, default = 20)
        args = parser.parse_args()

        page = args.page
        per_page = args.per_page

        args_without_page = args.pop('page')
        kwds = args_without_page.pop('per_page')
        results = CreatorModel.query().filter_by(**kwds).order_by(CreatorModel.id).all()
        if results is None:
            abort(404)

        results = results.paginate(page=page, per_page=per_page)

        return jsonify({
            'page': page,
            'per_page': per_page,
            'has_next': results.has_next,
            'has_prev': results.has_prev,
            'page_list': [iter_page if iter_page else '...' for iter_page in results.iter_pages()],
            'creators': CreatorSchema(many=True, exclude=['geo']).dump(results)})

