
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
    from .models import Report, AssignTask
    from app import db
    descriptions = (
        db.session
        .query(Report, AssignTask.priority)
        .filter_by(assignedTo=current_user.id)
        .join(AssignTask, AssignTask.issueId == Report.id)
        .all()
    )
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


document = ""
task_id = -1


@view.route('/document/<int:id>', methods=["GET", "POST"])
@login_required
def document(id):
    from .models import Report
    report = Report.query.get(id)
    global task_id
    task_id = id
    if request.method == "POST":
        global document
        document = request.form.get("document-content")
        return redirect(url_for('view.tasks'))

    return render_template('doc_area.html', report=report, id=id)


@view.route('/tasks', methods=["GET", "POST"])
@login_required
def tasks():
    global document
    global task_id
    from .models import Report, IssueStatus, AssignTask, Update
    from app import db

    reports = (
        db.session
        .query(Report, AssignTask.priority)
        .filter_by(assignedTo=current_user.id)
        .join(AssignTask, AssignTask.issueId == Report.id)
        .all()
    )

    if request.method == "POST":
        status = request.form.get('status')
        if not status:
            flash("Status cannot be empty choose an option", category='error')
        else:
            if not document or task_id == -1:
                flash("Document cannot be empty", category='error')
                return redirect(url_for('view.tasks'))

            else:
                issueStatus = IssueStatus(
                    status=status, documentation=document, issueId=task_id)

                db.session.add(issueStatus)
                db.session.commit()

                document = ""
            flash("Status updated successfully", category="success")

    return render_template('task.html', descriptions=reports, count=len(reports))
