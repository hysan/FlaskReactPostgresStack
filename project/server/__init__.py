# project/server/__init__.py

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/auth/*": {"origins": "http://localhost:3000"}})

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

@app.route('/api')
def api():
    return render_template('api.html')
