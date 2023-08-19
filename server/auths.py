import re
from flask import Blueprint, render_template, redirect, url_for, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')


@auth.route('/register', methods=["GET", "POST"])
def register():
    validate_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # pattern validate email
    validate_psswrd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"  # validate pass

    if request.method == "POST":

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')  # confirm password

        if not re.match(validate_email, email):
            flash('Invalid email', category="error")
        elif password1 != password2:
            flash('Password do not match', category="error")
        elif not re.match(validate_psswrd, password1):
            flash('Invalid password \n'
                  'at 8 characters long \n'
                  'at least one uppercase letter \n'
                  'at least one lowercase letter \n'
                  'at least one digit \n'
                  'at least one special character (e.g., !, @, #, $, etc.)'
                  , category="error")
        else:
            flash('Registered successfully', category="error")

    return render_template('register.html')


@auth.route('/logout')
def logout():
    print("logout success.")
    return redirect(url_for('view.home'))
