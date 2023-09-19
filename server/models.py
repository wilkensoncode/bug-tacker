from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class RegisteredUser(db.Model):
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
    issue_name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # get date by default




