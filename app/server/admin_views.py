import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import current_user, login_required
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
    return redirect('/admin/dashboard')


@admin_view.route('/admin/dashboard')
def dashboard():
    from .models import Report, Developer
    reports = Report.query.all()
    developers = Developer.query.all()
    count_reports = len(reports)
    count_developers = len(developers)
    print(count_reports, count_developers)
    return render_template('adm_dash.html', reports=reports, developers=developers, count_reports=count_reports, count_dev=count_developers)


@admin_view.route('/admin/charts')
def charts():
    return render_template('adm_charts.html')


@admin_view.route('/admin/dev', methods=["GET", "POST"])
def add_dev():
    from .models import User
    current_date = datetime.now()
    new_date = current_date + timedelta(weeks=1)
    users = User.query.all()
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        print(email)
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
            from .models import Developer, User
            from app import db
            developer = Developer.query.filter_by(email=email).first()
            print(User)
            if not developer:
                new_dev = Developer(
                    email=email,
                    salary=salary,
                    office=office,
                    position=position,
                    start_date=start_date)

                db.session.add(new_dev)
                db.session.commit()
                flash("Developer added successfully", category="success")
            else:
                flash("Developer already exist", category="error")

    return render_template('adm_add_dev.html', default_date=new_date.strftime("%Y-%m-%d"), users=users)


@admin_view.route('/admin/user-manage', methods=["GET", "POST"])
def update_info():
    if request.method == "POST":
        from .models import User, Update
        from app import db

        current_email = request.form.get("email")
        new_password = request.form.get("update_password")
        new_email = request.form.get("new_email")

        admin_password = request.form.get("admin_password")
        is_admin = request.form.get("is_admin")
        not_admin = request.form.get("not_admin")
        remove_user = request.form.get("remove_user")

        if current_user.admin == True:
            print("admin", current_user.admin)
            user = User.query.filter_by(email=current_email).first()
            if current_email and new_password and admin_password:
                if user:
                    if check_password_hash(current_user.password, admin_password):
                        user.password = generate_password_hash(
                            new_password, method='sha256')

                        update_info = Update(
                            affected_user_email=current_email,
                            admin_email=current_user.email,
                            operation="Update Password")

                        db.session.add(update_info)
                        db.session.commit()
                        flash("Password updated successfully",
                              category="success")
                    else:
                        flash("Invalid credentials", category="error")
                else:
                    flash("User does not exist", category="error")

            elif current_email and new_email and admin_password:
                if user:
                    if check_password_hash(current_user.password, admin_password):
                        user.email = new_email

                        update_info = Update(
                            affected_user_email=current_email,
                            admin_email=current_user.email,
                            operation="Update Email")

                        db.session.add(update_info)
                        db.session.commit()
                        flash("Email updated successfully", category="success")
                    else:
                        flash("Invalid credentials", category="error")
                else:
                    flash("User does not exist", category="error")

            elif current_email and is_admin and admin_password:
                if user:
                    if check_password_hash(current_user.password, admin_password):
                        user.admin = True
                        update_info = Update(
                            affected_user_email=current_email,
                            admin_email=current_user.email,
                            operation="Make user admin")

                        db.session.add(update_info)
                        db.session.commit()

                        flash("User is now an admin", category="success")
                    else:
                        flash("Invalid credentials", category="error")
                else:
                    flash("User does not exist", category="error")

            elif current_email and admin_password and not_admin and not is_admin and not new_email and not new_password:
                if user:
                    if check_password_hash(current_user.password, admin_password):
                        user.admin = False
                        update_info = Update(
                            affected_user_email=current_email,
                            admin_email=current_user.email,
                            operation="Remove admin privilege")

                        db.session.add(update_info)
                        db.session.commit()
                        flash("User is no longer an admin", category="success")
                    else:
                        flash("Invalid credentials", category="error")
                else:
                    flash("User does not exist", category="error")

            elif current_email and remove_user and admin_password and not not_admin and not is_admin and not new_email and not new_password:
                if user:
                    if check_password_hash(current_user.password, admin_password):
                        db.session.delete(user)

                        update_info = Update(
                            affected_user_email=current_email,
                            admin_email=current_user.email,
                            operation="Remove user")

                        db.session.add(update_info)
                        db.session.commit()
                        flash("User removed successfully", category="success")
                    else:
                        flash("Invalid credentials", category="error")
                else:
                    flash("User does not exist", category="error")

    return render_template('user_manage.html')


@admin_view.route('/admin/task', methods=["GET", "POST"])
def task():
    from .models import Report, Developer, Update, User, AssignTask
    from app import db

    reports = Report.query.all()
    developers = Developer.query.all()

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

            dev = Developer.query.filter_by(id=dev_id).first()
            report = Report.query.filter_by(id=bug_id).first()
            # user = User.query.filter_by(email=dev_id.email).first()
            print(dev.email)
            if dev and report:
                report.assignedTo = None

                update_info = Update(
                    affected_user_email=dev.email,
                    admin_email=current_user.email,
                    operation=f"Assign Task issue{bug_id}")

                db.session.add(update_info)
                db.session.commit()
                flash("Task assigned successfully", category="success")
            else:
                flash("Invalid IDs", category="error")

    return render_template('adm_assign.html', reports=reports, developers=developers)
