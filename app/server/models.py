from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(250))
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())
    email = db.Column(db.String(250), unique=True, index=True)
    developer = db.relationship('Developer', backref='user', lazy=True)
    AssignTask = db.relationship('AssignTask', backref='user', lazy=True)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250))
    issue_name = db.Column(db.String(100))
    url = db.Column(db.String(250))
    description = db.Column(db.String(500))
    # assignedTo = db.Column(db.Integer, db.ForeignKey('developer.id')))
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())


class IssueStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(15))
    documentation = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salary = db.Column(db.String(250))
    office = db.Column(db.String(100))
    position = db.Column(db.String(100))
    start_date = db.Column(db.DateTime(timezone=True), default=func.now())
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())
    email = db.Column(db.String(250), db.ForeignKey('user.email'))
    AssignTask = db.relationship('AssignTask', backref='developer', lazy=True)


class AssignTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issueId = db.Column(db.Integer, unique=True)
    DeveloperId = db.Column(db.Integer, db.ForeignKey('developer.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())


class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    affected_user_email = db.Column(db.String(250))
    admin_email = db.Column(db.String(250))
    operation = db.Column(db.String(250))
    date_created = db.Column(db.DateTime(timezone=True),
                             default=func.now())
