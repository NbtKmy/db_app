from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import db


ma = Marshmallow()


class DatabaselistModel(db.Model):
    __tablename__ = 'databaselist'


    id = db.Column(db.String(32), primary_key=True, nullable=False)
    title_ja = db.Column(db.String(128), nullable=False)
    title_en = db.Column(db.String(128))
    creator_id = db.Column(db.String(32))
    ddc_category = db.Column(db.String(32))
    type =db.Column(db.String(64))
    description_ja = db.Column(db.Text)
    description_en = db.Column(db.Text)
    url = db.Column(db.url, nullable=False)
    change_date = db.Column(db.DateTime)
    link_check = db.Column(db.String(2))
    

class DatabaselistSchema(ma.ModelSchema):
    class Meta:
        model = DatabaselistModel

    change_date = fields.DateTime('%Y-%m-%d')
    
