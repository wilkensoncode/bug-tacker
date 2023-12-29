from flask import Flask
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from .server.views import view
from .server.auths import auth

from .server.admin_views import admin_view
from .server.admin_auths import admin_auth
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

import os

# path to condig folder
config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')


for filename in os.listdir(config_dir):
    if filename.endswith('.env'):
        env_file_path = os.path.join(config_dir, filename)
        load_dotenv(env_file_path)

SECRET_KEY = os.getenv('SECRET_KEY')

db = SQLAlchemy()

IP = os.getenv('MYSQL_IP')
USERNAME = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASS')
DB_NAME = os.getenv('MYSQL_DB')


def create_app():
    app = Flask(__name__, template_folder='client/templates',
                static_folder='client/static')
    app.config['SECRET_KEY'] = SECRET_KEY
    DB_CONFIG_STR = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{IP}/{DB_NAME}"
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG_STR
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    app.register_blueprint(admin_view, url_prefix='/')
    app.register_blueprint(admin_auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .server.models import User

        return User.query.get(int(id))

    from .server import models

    with app.app_context():
        db.create_all()

        USER_FIRSTNAME = os.getenv('USER_FIRSTNAME')
        USER_LASTNAME = os.getenv('USER_LASTNAME')
        USER_EMAIL = os.getenv('USER_EMAIL')
        USER_PASSWORD = os.getenv('USER_PASSWORD')

        ADMIN_FIRSTNAME = os.getenv('ADMIN_FIRSTNAME')
        ADMIN_LASTNAME = os.getenv('ADMIN_LASTNAME')
        ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
        ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

        if not models.User.query.filter_by(email=ADMIN_EMAIL).first():

            admin = models.User(
                first_name=ADMIN_FIRSTNAME,
                last_name=ADMIN_LASTNAME,
                email=ADMIN_EMAIL,
                admin=True,
                password=generate_password_hash(
                    ADMIN_PASSWORD, method='sha256'),
            )
            db.session.add(admin)

        if not models.User.query.filter_by(email=USER_EMAIL).first():
            user = models.User(
                first_name=USER_FIRSTNAME,
                last_name=USER_LASTNAME,
                email=USER_EMAIL,
                admin=False,
                password=generate_password_hash(
                    USER_PASSWORD, method='sha256'),

            )
            db.session.add(user)

        db.session.commit()

    return app


app = create_app()
