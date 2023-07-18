from flask import Flask
from dotenv import load_dotenv
from website import config

from .server.views import view
from .server.auth import auth

import os

config_folder = os.path.dirname(os.path.abspath('./config'))

env_files = {
    'secret': os.path.join(config_folder, 'config', 'secret.env'),
    'zo': os.path.join(config_folder, 'config', 'zo.env')
}

for file_path in env_files:
    load_dotenv(env_files[file_path])

SECRET_KEY = os.getenv('SECRET_KEY')
API = os.getenv("API")


def create_app():
    app = Flask(__name__, template_folder='client/templates')
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


