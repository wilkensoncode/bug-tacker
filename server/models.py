from website import db

from flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    first_last = db.Column(db.String(100))
    email = db.Column(db.String(250))
    password1 = db.Column(db.String(250))
    password2 = db.Column(db.String(250))


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    issue_name = db.Column(db.String(100))




