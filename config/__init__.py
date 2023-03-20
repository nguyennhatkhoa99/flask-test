import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = os.getenv("DEBUG") or False
    TESTING = os.getenv("TESTING") or False
    SECRET_KEY = os.environ['SECRET_KEY'] or 'secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
