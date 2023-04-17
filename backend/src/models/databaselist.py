from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import Base
from .creator import *


ma = Marshmallow()


class DatabaselistModel(Base):
    __tablename__ = 'databaselist'

    id = Column(String(32), primary_key=True, nullable=False)
    title_ja = Column(String(128), nullable=False)
    title_en = Column(String(128))
    creator_id = Column(String(32), ForeignKey('creator.id'))
    ddc_category = Column(String(32))
    media_type = Column(String(64))
    description_ja = Column(Text)
    description_en = Column(Text)
    url = Column(String(128), nullable=False)
    change_date = Column(DateTime)
    link_check = Column(String(2))


class DatabaselistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DatabaselistModel
        load_instance = True

    change_date = fields.DateTime('%Y-%m-%d')
    creator = fields.Nested('CreatorSchema', only=('name_ja', 'name_en'))
    
