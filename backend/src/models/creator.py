from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db
import uuid
from sqlalchemy import func
from sqlalchemy.types import UserDefinedType

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

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name_ja = db.Column(db.String(128), nullable=False)
    name_en = db.Column(db.String(128))
    geo = db.Column(db.Point)
    altnames = db.Column(db.String(256))
    wikidata_id = db.Column(db.String(32))
    change_date = db.Column(db.DateTime)


class CreatorSchema(ma.ModelSchema):
    class Meta:
        model = CreatorModel

    change_date = fields.DateTime('%Y-%m-%d')
    lat = fields.Method('get_lat')
    lon = fields.Method('get_lon')

    def get_lat(self, obj):
        x = 6
        y = obj.geo.index(' ')
        lat = obj.geo[x:y]
        return lat
    
    def get_lon(self, obj):
        s = obj.geo.index(' ') + 1
        t = obj.geo.index(')')
        lon = obj.geo[s:t]
        return lon
