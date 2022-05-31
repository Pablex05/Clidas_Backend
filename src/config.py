class DevelopmentConfig:
    # Mode debug
    DEBUG = True
    # Port App
    PORT = 5000
    # database config
    # database user
    MYSQL_DATABASE_USER = 'root'
    # database password
    MYSQL_DATABASE_PASSWORD = 123456789
    # database name
    MYSQL_DATABASE_DB = 'flask_blog'
    # database host
    MYSQL_DATABASE_HOST = 'localhost'
    # connection database
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}'
    # track modifications in objects
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # secret key
    SECRET_KEY = '1234'

config = {
    'development': DevelopmentConfig
}