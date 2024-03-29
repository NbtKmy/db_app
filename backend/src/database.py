from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@mysql:3306/{database}?charset=utf8mb4'.format(
      user=os.getenv('MYSQL_USER'),
      password=os.getenv('MYSQL_PASSWORD'),
      database=os.getenv('MYSQL_DATABASE')
    )

engine = create_engine(
  SQLALCHEMY_DATABASE_URI,
  echo=False
  )


session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = session.query_property()


def init_db():
    
    #import .models.creator
    #import .models.databaselist
    from src import models
    
    Base.metadata.create_all(bind=engine)