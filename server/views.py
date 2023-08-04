from flask import Blueprint, render_template, redirect, url_for

view = Blueprint('view', __name__)


# client
@view.route('/')
def home():
    return render_template('index.html')


@view.route('/login')
def login():
    return render_template('login.html')


@view.route('/logout')
def logout():
    return redirect(url_for('view.home'))


@view.route('/register')
def register():
    return render_template('register.html')


@view.route('/issues')
def issues():
    return render_template('issues.html')


@view.route('/team')
def team():
    return render_template('team.html')


@view.route('/report')
def report():
    return render_template('report.html')
