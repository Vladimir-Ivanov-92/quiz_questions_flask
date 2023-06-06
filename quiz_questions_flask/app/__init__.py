import os

from flask import Flask

from .extensions import db

config_dispatcher = {
    "development": "config.DevelopmentConfig",
    "production": "config.ProductionConfig"
    # add more dispatchers here
}

def register_blueprints(app):
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ.get("FLASK_ENV") or config_dispatcher['development'])
    db.init_app(app)
    register_blueprints(app)
    return app


def setup_database(app):
    """Первоначальное создание базы данных"""
    with app.app_context():
        db.create_all()

from . import db_data, extensions, models