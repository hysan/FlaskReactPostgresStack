# project/server/__init__.py

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.server.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
from project.server.methodview.views import methodview_blueprint
app.register_blueprint(methodview_blueprint, url_prefix='/methodview')
from project.server.route.views import route_blueprint
app.register_blueprint(route_blueprint, url_prefix='/route')

from flask import render_template

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')