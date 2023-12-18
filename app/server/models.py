from app import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    first_last = db.Column(db.String(100))
    email = db.Column(db.String(250))
    admin = db.Column(db.Boolean, default=False)
    password1 = db.Column(db.String(250))
    password2 = db.Column(db.String(250))


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    issue_name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True),
                     default=func.now())  # get date by default


class IssueStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(15))


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(250))
    salary = db.Column(db.String(250))
    office = db.Column(db.String(100))
    position = db.Column(db.String(100))
    start_date = db.Column(db.String(100))


class AssignTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issueId = db.Column(db.Integer)
    DeveloperId = db.Column(db.Integer)
    priority = db.Column(db.String(100))
