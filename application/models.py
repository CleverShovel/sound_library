from . import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)

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
