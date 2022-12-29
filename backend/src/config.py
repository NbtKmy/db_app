import os


class DevelopmentConfig:

  # SQLAlchemy
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(
    **{
      'user': os.getenv('MYSQL_USER', 'root'),
      'password': os.getenv('MYSQL_PASSWORD', 'hoge'),
      'host': os.getenv('DB_HOST', 'db'),               # 後で調べる
      'database': os.getenv('MYSQL_DATABASE', 'hoge'),
    })
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False


Config = DevelopmentConfig