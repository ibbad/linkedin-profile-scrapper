"""
Initialize the application and api blueprints
"""
from flask import Flask
from config import config


def create_app(config_name='default', **config_overrides):
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config[config_name])
    # Override configurations with **kwargs
    app.config.update(config_overrides)
    config[config_name].init_app(app)

    # Register blueprints
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app