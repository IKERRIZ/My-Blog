from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # app configuration
    app.config.from_object(config_options[config_name]) 

    # initializing flask extensions
    bootstrap.init_app(app)

    #registering the main app blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app