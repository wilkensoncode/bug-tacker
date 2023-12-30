import re

from flask import render_template, Blueprint, flash, request, redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user
admin_auth = Blueprint('admin_auth', __name__)


@admin_auth.route('/admin/login', methods=["GET", "POST"])
def adm_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        from .models import User
        user = User.query.filter_by(email=email).first()

        if user and user.admin == True:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('admin_view.dashboard'))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Incorrect credential", category="error")

    return render_template('adm_login.html')


@admin_auth.route('/admin/logout', methods=["GET", "POST"])
def adm_logout():
    logout_user()
    return render_template('adm_login.html')
