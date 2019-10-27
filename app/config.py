import os
class Config:
    '''
    General configuration parent class
    '''
    QUOTES_BASE_URL =os.environ.get('QUOTES_BASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:7552@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

