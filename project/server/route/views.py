# project/server/route/views.py


from flask import Blueprint, render_template

route_blueprint = Blueprint('route', __name__)

@route_blueprint.route("/route")
def example_route():
    return "hello world route"

@route_blueprint.route('/route/index')
def example_template_route():
    return render_template('index.html')