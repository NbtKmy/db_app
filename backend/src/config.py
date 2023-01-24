import os


class Config:

  # SQLAlchemy
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@mysql:3306/{database}?charset=utf8mb4'.format(
    **{
      'user': os.getenv('MYSQL_USER'),
      'password': os.getenv('MYSQL_PASSWORD'),
      'host': os.getenv('DB_HOST'), 
      'database': os.getenv('MYSQL_DATABASE'),
    })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False


Config = Config