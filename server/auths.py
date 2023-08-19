from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    print("logout success.")
    return redirect(url_for('view.home'))


@auth.route('/register')
def register():
    return render_template('register.html')
