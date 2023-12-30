
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
view = Blueprint('view', __name__)


@view.route('/')
def home():
    return render_template('index.html')


@view.route('/issues', methods=["GET", "POST"])
@login_required
@login_required
def issues():
    from .models import Report
    descriptions = Report.query.all()
    return render_template('issues.html', descriptions=descriptions, count=len(descriptions))


@view.route('/team')
@login_required
@login_required
def team():
    from app import db
    from .models import Developer, User
    developers = db.session.query(Developer, User).join(
        User, User.email == Developer.email).all()
    for developer, user in developers:
        print(developer, user)

    return render_template('team.html', developers=developers)


@view.route('/report', methods=["GET", "POST"])
@login_required
@login_required
def report():
    if request.method == "POST":
        email = request.form.get("email")
        issue_name = request.form.get("issue")
        url = request.form.get("url")
        description = request.form.get("description")

        if not email or not issue_name or not url or not description:
            flash("All fields are required", category="error")
        else:
            from .models import Report
            from app import db
            new_report = Report(
                email=email, issue_name=issue_name, url=url, description=description)

            db.session.add(new_report)
            db.session.commit()

            flash("Report submitted successfully", category="success")

    return render_template('report.html')


@view.route('/subscribe')
def subscribe():
    print("subscribe")
    return redirect(url_for('view.home'))


@view.route('/document', methods=["GET", "POST"])
@login_required
def document():
    if request.method == "POST":
        print("document")
        return redirect(url_for('view.tasks'))

    return render_template('doc_area.html')


@view.route('/tasks', methods=["GET", "POST"])
@login_required
def tasks():
    from .models import Report, Developer

    reports = Report.query.filter_by(assignedTo=current_user.id).all()
    print(reports, len(reports), current_user.id, current_user.email)
    if request.method == "POST":
        status = request.form.get('status')

        if not status:
            flash("Status cannot be empty choose an option", category='error')
        else:
            flash("Status updated successfully", category="success")

    return render_template('task.html', descriptions=reports, count=len(reports))
