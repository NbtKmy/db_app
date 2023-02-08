from flask_restful import Resource, abort
from flask import jsonify, request
from src.models.creator import CreatorModel, CreatorSchema
import math


class CreatorAllAPI(Resource):

    def get(self):
        results = CreatorModel.query.all()
        return jsonify({'creators': CreatorSchema(many=True, exclude=['geo']).dump(results)})


class CreatorAPI(Resource):
    
    def get(self):
        
        kwds_Multidict = request.args
        page = kwds_Multidict.get('page', default=1, type=int)
        per_page = kwds_Multidict.get('per_page', default=20, type=int)
        idStr = kwds_Multidict.get('id', default=None, type=str)
        name_jaStr = kwds_Multidict.get('name_ja', default=None, type=str)
        name_enStr = kwds_Multidict.get('name_en', default=None, type=str)
        altnamesStr = kwds_Multidict.get('altnames', default=None, type=str)

        kwds_dict = { 'id': idStr, 'name_ja': name_jaStr, 'name_en': name_enStr, 'altnames': altnamesStr }
        results = CreatorModel.query
        for key, value in kwds_dict.items():
            if value is None:
                continue
            results = results.filter(getattr(CreatorModel, key).like('%%%s%%' % value))
        
        
        if results is None:
            abort(404)

        results = results.order_by(CreatorModel.id)
        rows = results.count()
        offset_index = (page-1)*per_page
        results = results.limit(per_page).offset(offset_index)

        # has_next -> 0 = no next page ; 1 = next page exists
        if (offset_index + per_page) >= rows:
            has_next = 0
        else: 
            has_next = 1 

        # has_prev -> 0 = no prev page ; 1 = prev page exists
        if offset_index == 0:
            has_prev = 0
        else:
            has_prev = 1
        
        page_num = math.ceil(rows/per_page)
        # page errors
        if page > page_num:
            abort(404)
        elif page < 0:
            abort(404)
        else:
            pass

        return jsonify({
            'page': page,
            'per_page': per_page,
            'has_next': has_next,
            'has_prev': has_prev,
            'max_page_number': page_num,
            'creators': CreatorSchema(many=True, exclude=['geo']).dump(results)})

