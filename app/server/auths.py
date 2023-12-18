import re
from flask import Blueprint, render_template, redirect, url_for, request, flash, get_flashed_messages

from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import random

auth = Blueprint('auth', __name__)


def validate_credential(email=None, password=None):
    validate_email = r"^[a-zA-Z0-9.%_+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    validate_psswrd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
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
            flash("Email field cannot be empty", category="error")
            return
        elif password == '':
            flash("Password field cannot be empty", category="error")
            return
        elif not validate_credential(email, None):
            flash("Invalid Email", category="error")
        elif not validate_credential(None, password):
            flash("Wrong password", category="error")
            return
        else:
            from .models import User
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password1, password):
                    login_user(user, remember=True)

                    return redirect(url_for('view.issues'))
                else:
                    flash("Wrong password", category="error")
                    return redirect(url_for('auth.login'))
            else:
                flash("Email does not exist create an account ", category="error")
                return redirect(url_for('auth.register'))

    return render_template('login.html')


@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not validate_credential(email=email):
            flash('Invalid email -> examplename@gmail.com', category="error")
        elif password1 != password2:
            flash(
                'Password must be the same', category="error")
        elif not validate_credential(password=password1):
            flash("""Invalid password: ->  
            At least 8 characters long 
            Contains at least one special character (e.g., !, @, #, $, etc.) and at least a number""", category="error")
        else:
            from .models import User
            from app import db
            # need to check if email already exist
            # need to check if username already exist
            # email verification

            new_user = User(first_name=first_name, last_name=last_name, email=email,
                            password1=generate_password_hash(
                                password1, method='sha256'),
                            username=username)

            db.session.add(new_user)
            db.session.commit()

            flash('Registered Successfully', category="success")

    return render_template('register.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('view.home'))
