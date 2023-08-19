from flask import Blueprint, render_template, redirect, url_for

view = Blueprint('view', __name__)


# client
@view.route('/')
def home():
    return render_template('index.html')


@view.route('/issues')
def issues():
    return render_template('issues.html')


@view.route('/team')
def team():
    return render_template('team.html')


@view.route('/report')
def report():
    return render_template('report.html')
