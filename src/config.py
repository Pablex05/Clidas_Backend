class DevelopmentConfig:
    DEBUG = True
    PORT = 5000
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 123456789
    MYSQL_DATABASE_DB = 'flask_blog'
    MYSQL_DATABASE_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(MYSQL_DATABASE_USER, MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_HOST, MYSQL_DATABASE_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234'

config = {
    'development': DevelopmentConfig
}