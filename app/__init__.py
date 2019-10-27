from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options, DevConfig
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()

db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # app configuration
    app.config.from_object(config_options[config_name]) 

    # Setting app configurations
    app.config.from_object(DevConfig)

    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #registering the main app blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering the auth blueprint
    from .auth import auth as main_bluprint
    app.register_blueprint(main_bluprint, url_prefix = '/auth')


    return app