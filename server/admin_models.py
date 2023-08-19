from website import db


class UserAdmin(db.Model):
    id = db.Column(db.Intger, primary_key=True)
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))


class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(250))
    office = db.Column(db.String(100))
    position = db.Column(db.String(100))
    start_date = db.Column(db.String(100))


class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salary = db.Column(db.String(100))


class Issue(db.Model):
    id = db.Column(db.Integer, primay_key=True)
    status = db.Column(db.String(100))
    priority = db.Column(db.String(100))
    assign = db.Column(db.String(100))
