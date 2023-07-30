from flask import render_template, Blueprint

admin_auth = Blueprint('admin_auth', __name__)


@admin_auth.route('/admin/login')
def adm_login():
    return render_template('adm_login.html')
