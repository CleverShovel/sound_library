from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import makedirs

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    makedirs(app.config['SOUND_FOLDER'], exist_ok=True)
    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Imports
        from . import routes
        from . import auth
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create tables for our models
        db.create_all()

        return app
