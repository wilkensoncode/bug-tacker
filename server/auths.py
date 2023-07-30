from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('adm_login.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')



