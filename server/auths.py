import re
from flask import Blueprint, render_template, redirect, url_for, request, flash, get_flashed_messages

auth = Blueprint('auth', __name__)


def validate_credential(email=None, password=None):
    validate_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # pattern validate email
    validate_psswrd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"  # validate pass
    if email and not password:
        return re.match(validate_email, email)
    elif password and not email:
        return re.match(validate_psswrd, password)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')
        if email == '':
            flash("Email field cannot be empty", category="warning")
        elif password == '':
            flash("Password field cannot be empty", category="warning")
        elif not validate_credential(email, None):
            flash("Invalid Email", category="error")
        elif not validate_credential(None, password):
            flash("Wrong password", category="success")

    return render_template('login.html')


@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')  # confirm password

        if not validate_credential(email, None):
            flash('Invalid email -> examplename@gmail.com', category="error")
        elif password1 != password2:
            flash('Password do not match Fild One and Field Two must be the same', category="error")
        elif not validate_credential(None, password1):
            flash("""Invalid password: ->  
            At least 8 characters long 
            Contains at least one special character (e.g., !, @, #, $, etc.) and at least a number"""
                  , category="error")
        else:
            flash('Registered Successfully', category="success")

    return render_template('register.html')


@auth.route('/logout')
def logout():
    print("logout success.")
    return redirect(url_for('view.home'))
