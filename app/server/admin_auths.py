import re

from flask import render_template, Blueprint, flash, request, redirect, url_for
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
admin_auth = Blueprint('admin_auth', __name__)


def validate_credential(email=None, password=None):
    # pattern validate email
    validate_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # validate pass
    validate_psswrd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if email and not password:
        return re.match(validate_email, email)
    elif password and not email:
        return re.match(validate_psswrd, password)


@admin_auth.route('/admin/login', methods=["GET", "POST"])
def adm_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not validate_credential(email, None):
            flash("Invalid email", category="error")
        if not validate_credential(None, password):
            flash("Invalid password", category="error")
        else:
            from .models import User
            user = User.query.filter_by(email=email).first()
            if user and current_user.admin == True:
                if check_password_hash(user.password, password):
                    flash("Login successful", category="success")
                    return redirect(url_for('admin_view.dashboard'))
                else:
                    flash("Incorrect password", category="error")

    return render_template('adm_login.html')
