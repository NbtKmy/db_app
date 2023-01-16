from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import db
from sqlalchemy import func
from sqlalchemy.types import UserDefinedType
from src.models.databaselist import DatabaselistModel, DatabaselistSchema

ma = Marshmallow()

# Create a custom Point type
class Point(UserDefinedType):
    def get_col_spec(self):
        return "POINT"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ST_AsText(col, type_=self)

class CreatorModel(db.Model):
    __tablename__ = 'creator'

    id = db.Column(db.String(32), primary_key=True, nullable=False)
    name_ja = db.Column(db.String(128), nullable=False)
    name_en = db.Column(db.String(128))
    geo = db.Column(db.Point)
    altnames = db.Column(db.String(256))
    wikidata_id = db.Column(db.String(32))
    change_date = db.Column(db.DateTime)

    databases = db.relationship(DatabaselistModel, backref='creator', lazy=True)


class CreatorSchema(ma.ModelSchema):
    class Meta:
        model = CreatorModel

    change_date = fields.DateTime('%Y-%m-%d')
    lat = fields.Method('get_lat')
    lon = fields.Method('get_lon')
    databases = fields.Nested(DatabaselistSchema, many=True, exculde=('creator_id', 'creator',))

    def get_lat(self, obj):
        x = 6                   # The string 'POINT(' should be removed 
        y = obj.geo.index(' ')
        lat = obj.geo[x:y]
        return lat
    
    def get_lon(self, obj):
        s = obj.geo.index(' ') + 1
        t = obj.geo.index(')')
        lon = obj.geo[s:t]
        return lon
