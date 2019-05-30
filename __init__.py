from flask import Flask
from .config import Config
from .application.home import home_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprints(app)
    context_processor(app)

    return app


def register_blueprints(app):
    app.register_blueprint(home_bp)


def register_extensions(app):
    pass


def register_db(app):
    pass


def context_processor(app):
    @app.context_processor
    def index():
        return {
            'blog_name': '我的个人博客'
        }