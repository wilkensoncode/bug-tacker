from flask import render_template, Blueprint

admin_view = Blueprint('admin_view', __name__)


@admin_view.route('/admin')
def admin():
    return render_template('adm_dash.html')


@admin_view.route('/admin/dashboard')
def dashboard():
    return render_template('adm_dash.html')


@admin_view.route('/admin/dev')
def add_dev():
    return render_template('adm_add_dev.html')


@admin_view.route('/admin/reset')
def reset_pass():
    return render_template('adm_password.html')

