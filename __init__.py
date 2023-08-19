from flask import Flask
from dotenv import load_dotenv
from website import config

from .server.views import view
from .server.auths import auth
# admin
from .server.admin_views import admin_view
from .server.admin_auths import admin_auth

import os

#  get path to config directory
config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')

# Loop through files in the config directory
for filename in os.listdir(config_dir):
    # Check if file has a .env extension
    if filename.endswith('.env'):
        # Load environment variables from file
        env_file_path = os.path.join(config_dir, filename)
        load_dotenv(env_file_path)

SECRET_KEY = os.getenv('SECRET_KEY')  # set secret key


def create_app():
    app = Flask(__name__, template_folder='client/templates', static_folder='client/static')
    app.config['SECRET_KEY'] = SECRET_KEY  # set secret key

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin_view, url_prefix='/')
    app.register_blueprint(admin_auth, url_prefix='/')

    return app
