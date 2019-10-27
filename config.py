from os import environ, path, getenv
basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI',
                                     'sqlite:///' + path.join(basedir, 'app.db'))
    SQLALCHEMY_MIGRATE_REPO = getenv('SQLALCHEMY_MIGRATE_REPO',
                                     path.join(basedir, 'db_repository'))

    # Files
    SOUND_FOLDER = getenv('SOUND_FOLDER', path.join(basedir, 'sound_files/'))
