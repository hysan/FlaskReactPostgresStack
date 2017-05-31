# project/server/route/views.py


from flask import Blueprint, render_template

from project.server.auth.decorators import jwt_auth

route_blueprint = Blueprint('route', __name__)

@route_blueprint.route("/")
def example_route():
    return "hello world route"

@route_blueprint.route('/index')
def example_template_route():
    return render_template('index.html')

@route_blueprint.route("/jwt")
@jwt_auth(return_user_id=True)
def example_route_with_jwt(user_id):
    return 'hello world route with user_id: {0}'.format(user_id)

@route_blueprint.route('/jwtindex')
@jwt_auth()
def example_template_route_with_jwt():
    return render_template('index.html')
