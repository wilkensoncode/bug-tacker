from website import db  

class UserAdmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    urer_name = 'root'
    email = "root@bug.com"
    password = "Testing!"


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
