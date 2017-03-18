import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '122334'
    SQLALCHEMY_COMMIT_ON_TEARDOW = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    db_user = 'postgres'
    db_pass = '122334'
    db_host = 'localhost'
    db_database = 'datacenter'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'+ Config.db_user +':'+ Config.db_pass +'@'+ Config.db_host +'/'+ Config.db_database

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + Config.db_user + ':' + Config.db_pass + '@' + Config.db_host +'/'+ Config.db_database

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + Config.db_user + ':' + Config.db_pass + '@' + Config.db_host +'/'+ Config.db_database

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}