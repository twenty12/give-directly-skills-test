from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    request = db.relationship('Request', backref='user', lazy=True)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise AssertionError('Provided email is not an email address')
        return email


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    request = db.relationship('Request', backref='book', lazy=True)


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)
    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow)
    book_id = db.Column(
        db.Integer,
        db.ForeignKey('book.id'),
        nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False)
