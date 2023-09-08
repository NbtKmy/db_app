from sqlalchemy import Column, String, Text, ForeignKey
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import Base
from src.models.creator import *


ma = Marshmallow()

class MapModel(Base):
    __tablename__ = 'databaselist'

    id = Column(String(32), primary_key=True, nullable=False)
    title_ja = Column(String(128), nullable=False)
    creator_name_ja = Column(String(32), ForeignKey('creator.name_ja'))
    creator_geo = Column(Point, ForeignKey('creator.geo'))
    description_ja = Column(Text)
    url = Column(String(128), nullable=False)

class MapSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MapModel
        model_converter = PointConverter
        load_instance = True

    lat = fields.Method('get_lat_float')
    lon = fields.Method('get_lon_float')

    def get_lat_float(self, obj):
        if obj.geo is None:
            lat = None
            return lat
        else:
            x = 0                   
            y = obj.geo.index(',')
            lat = float(obj.geo[x:y])
            return lat
    
    def get_lon_float(self, obj):
        if obj.geo is None:
            lon = None
            return lon
        else:
            s = obj.geo.index(' ') + 1
            lon = float(obj.geo[s:])
            return lon
    


