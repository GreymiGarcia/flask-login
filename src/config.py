class Config:
    SECRET_KEY = 'NB·hYuNknxzOVuh8sl(2qnjVqawTO1R='
class developmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask-login'
    MYSQL_CURSORCLASS = "DictCursor"

config = {
    'development':developmentConfig
}