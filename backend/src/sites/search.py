from flask import render_template, request
from sqlalchemy import or_
from src.models.databaselist import DatabaselistModel, DatabaselistSchema


def search():

    text_input = request.args.get('search')
    if text_input is None:
        results = None
    elif len(text_input) == 0:
        results = DatabaselistModel.query.all()
    else:
        results = DatabaselistModel.query.filter(or_(getattr(DatabaselistModel, 'title_ja').like('%%%s%%' % text_input), getattr(DatabaselistModel, 'description_ja').like('%%%s%%' % text_input))).all()
    

    return render_template('search.html', results=results)