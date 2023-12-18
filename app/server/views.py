from flask import Blueprint, render_template, url_for, redirect, request, flash

view = Blueprint('view', __name__) 

# client
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

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        issue_name = request.form.get("issue")
        description = request.form.get("description")
        if first_name == "":
            flash("Firstname cannot be empty", category="error")
        elif len(first_name) < 2:
            flash("Firstname must be at least 2 characters long", category="error")
        elif last_name == "":
            flash("Lastname cannot be empty", category="error")
        elif len(last_name) < 2:
            flash("Lastname must be at least 2 characters long", category="error")
        elif len(issue_name) < 2 or len(issue_name) > 15:  # min 2 max 15 char long
            flash("Minimum / Maximum characters = 2 / 15 ", category="error")
        elif issue_name == "":
            flash("Issue cannot be empty", category="error")
        elif description == "":
            flash("Description cannot be empty", category="error")

    return render_template('report.html')


@view.route('/subscribe')
def subscribe():
    print("subscribe")
    return redirect(url_for('view.home'))
