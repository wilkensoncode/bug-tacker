import re

from flask import render_template, Blueprint, flash, request

admin_auth = Blueprint('admin_auth', __name__)


def validate_credential(email=None, password=None):
    validate_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # pattern validate email
    validate_psswrd = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"  # validate pass
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
            pass

    return render_template('adm_login.html')
