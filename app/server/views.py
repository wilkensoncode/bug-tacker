
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user
view = Blueprint('view', __name__)


@view.route('/')
def home():
    return render_template('index.html')


@view.route('/issues', methods=["GET", "POST"])
def issues():
    if request.method == "POST":
        status = request.form.get('status')
        if not status:
            flash("Status cannot be empty choose an option", category='error')
        else:
            flash("Status updated successfully", category="success")

    return render_template('issues.html')


@view.route('/team')
def team():
    return render_template('team.html')


@view.route('/report', methods=["GET", "POST"])
def report():
    not_guess = ""
    if current_user.is_authenticated:
        not_guess = current_user.email

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

    return render_template('report.html', not_guess=not_guess)


@view.route('/subscribe')
def subscribe():
    print("subscribe")
    return redirect(url_for('view.home'))
