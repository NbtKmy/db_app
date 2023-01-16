from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from marshmallow_sqlalchemy.convert import ModelConverter
from src.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.types import UserDefinedType
from .databaselist import DatabaselistModel, DatabaselistSchema

ma = Marshmallow()

# Create a custom Point type
class Point(UserDefinedType):
    def get_col_spec(self):
        return "POINT"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ST_AsText(col, type_=self)

    def bind_processor(self, dialect):
        def process(value):
            if value is None:
                return None
            assert isinstance(value, str)
            lat, lng = value.split(', ')
            return "POINT(%s %s)" % (lng, lat)
        return process
    
    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None:
                return None
            #m = re.match(r'^POINT\((\S+) (\S+)\)$', value)
            #lng, lat = m.groups()
            lng, lat = value[6:-1].split()  # 'POINT(135.00 35.00)' => ('135.00', '35.00')
            geo = str(lat) + ', ' + str(lng)
            return geo
        return process

class CreatorModel(Base):
    __tablename__ = 'creator'

    id = Column(String(32), primary_key=True, nullable=False)
    name_ja = Column(String(128), nullable=False)
    name_en = Column(String(128))
    geo = Column(Point)
    altnames = Column(String(256))
    wikidata_id = Column(String(32))
    change_date = Column(DateTime)

    databases = relationship('DatabaselistModel', backref='creator', lazy=True)

class PointConverter(ModelConverter):
    SQLA_TYPE_MAPPING = dict(
        list(ModelConverter.SQLA_TYPE_MAPPING.items()) +
        [(Point, fields.Str)]
    )

class CreatorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CreatorModel
        model_converter = PointConverter
        load_instance = True

    change_date = fields.DateTime('%Y-%m-%d')
    lat = fields.Method('get_lat')
    lon = fields.Method('get_lon')
    databases = fields.Nested('DatabaselistSchema', many=True, exculde=('creator_id', 'creator',))

    def get_lat(self, obj):
        x = 0                   
        y = obj.geo.index(',')
        lat = obj.geo[x:y]
        return lat
    
    def get_lon(self, obj):
        s = obj.geo.index(' ') + 1
        lon = obj.geo[s:]
        return lon
