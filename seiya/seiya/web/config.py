class BaseConfig(object):
    SECRET_KEY = 'makesure set a very secret key'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/seiya?charset=utf8'

configs = { 
        'development': DevelopmentConfig
        }
