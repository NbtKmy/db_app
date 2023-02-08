from flask_restful import Resource, abort
from flask import jsonify, request
from src.models.databaselist import DatabaselistModel, DatabaselistSchema
import math



class DatabaselistAllAPI(Resource):


    def get(self):
        results = DatabaselistModel.query.all()
        return jsonify({'databaselist': DatabaselistSchema(many=True).dump(results)})


class DatabaselistAPI(Resource):
    
    def get(self):

        kwds_Multidict = request.args
        page = kwds_Multidict.get('page', default=1, type=int)
        per_page = kwds_Multidict.get('per_page', default=20, type=int)
        idStr = kwds_Multidict.get('id', default=None, type=str)
        title_jaStr = kwds_Multidict.get('title_ja', default=None, type=str)
        title_enStr = kwds_Multidict.get('title_en', default=None, type=str)
        creator_id = kwds_Multidict.get('creator_id', default=None, type=str)
        ddcStr = kwds_Multidict.get('ddc_category', default=None, type=str)
        typeStr = kwds_Multidict.get('type', default=None, type=str)
        description_jaStr = kwds_Multidict.get('description_ja', default=None, type=str)
        description_enStr = kwds_Multidict.get('description_en', default=None, type=str)

        kwds_dict = { 'id': idStr, 'title_ja': title_jaStr, 'title_en': title_enStr, 'creator_id': creator_id, 'ddc': ddcStr, 'type': typeStr, 'description_ja': description_jaStr, 'description_en': description_enStr }
        results = DatabaselistModel.query
        for key, value in kwds_dict.items():
            if value is None:
                continue
            results = results.filter(getattr(DatabaselistModel, key).like('%%%s%%' % value))
        
        
        if results is None:
            abort(404)

        results = results.order_by(DatabaselistModel.id)
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


        return jsonify({
            'page': page,
            'per_page': per_page,
            'has_next': has_next,
            'has_prev': has_prev,
            'max_page_number': page_num,
            'databases': DatabaselistSchema(many=True).dump(results)})