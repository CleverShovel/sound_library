from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = 'flasklogin-users'

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String,
                     nullable=False,
                     unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Sound(db.Model):
    """Model for track information."""

    ___tablename___ = 'sounds'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(255),
                     index=False,
                     unique=False,
                     nullable=False)
    path = db.Column(db.String(1024),
                     index=False,
                     unique=True,
                     nullable=False)

    def __repr__(self):
      return '<Sound {}>'.format(self.name)
