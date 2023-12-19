import re

from flask import render_template, Blueprint, request, flash
from datetime import datetime, timedelta
admin_view = Blueprint('admin_view', __name__)


def validate_credential(email=None, password=None):
    # pattern validate email
    validate_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # validate pass
    validate_psswrd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if email and not password:
        return re.match(validate_email, email)
    elif password and not email:
        return re.match(validate_psswrd, password)


@admin_view.route('/admin')
def admin():
    return render_template('adm_dash.html')


@admin_view.route('/admin/dashboard')
def dashboard():
    return render_template('adm_dash.html')


@admin_view.route('/admin/charts')
def charts():
    return render_template('adm_charts.html')


@admin_view.route('/admin/dev', methods=["GET", "POST"])
def add_dev():
    current_date = datetime.now()
    new_date = current_date + timedelta(weeks=1)
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        salary = request.form.get("salary")
        office = request.form.get("office")
        position = request.form.get("position")
        start_date = request.form.get("start_date")

        if first_name == "":
            flash("Firstname cannot be empty", category="error")
        elif last_name == "":
            flash("Lastname cannot be empty", category="error")
        elif not validate_credential(email, None):
            flash("Invalid Email", category="error")
        elif salary == '' or not salary.isdigit():
            flash("Invalid Salary", category="error")
        elif office == "":
            flash("Invalid office", category="error")
        elif position == '':
            flash("Invalid position", category="error")
        elif start_date == "":
            flash("Invalid start date", category="Error")
        else:
            from .models import Developer
            from app import db
            new_dev = Developer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                salary=salary,
                office=office,
                position=position,
                start_date=start_date)

            db.session.add(new_dev)
            db.session.commit()
            flash("Developer added successfully", category="success")

    return render_template('adm_add_dev.html', default_date=new_date.strftime("%Y-%m-%d"))


@admin_view.route('/admin/reset', methods=["GET", "POST"])
def reset_pass():
    print(request.form)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not validate_credential(email):
            flash("Invalid email", category="error")
        if not validate_credential(None, password):
            flash("Invalid password", category="error")
        else:
            flash("Password updated successfully")

    return render_template('adm_password.html')


@admin_view.route('/admin/task', methods=["GET", "POST"])
def task():
    print(request.form)
    if request.method == "POST":
        bug_id = request.form.get('bug_id')
        dev_id = request.form.get('dev_id')
        priority = request.form.get('priority')
        if bug_id == '':
            flash("Bug ID cannot be empty", category="error")
        elif dev_id == '':
            flash("Dev ID cannot be empty", category="error")
        elif not priority:
            flash("Priority cannot be empty", category="error")
        else:
            flash("Assign Task successfully", category="success")

    return render_template('adm_assign.html')
