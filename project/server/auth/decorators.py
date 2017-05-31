from functools import wraps
from flask import request, make_response, jsonify

from project.server.models import User

# This is the recommended coding style seen in the Flask docs for writing decorators:
# http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/#templating-decorator
def jwt_auth(return_user_id=False):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # get the auth token
            try:
                auth_header = request.headers.get('Authorization')
                if auth_header:
                    auth_token = auth_header.split(" ")[1]
                else:
                    auth_token = ''
            except Exception as e:
                # Failed to get the auth token. Could be formatting, etc.
                responseObject = {
                    'status': 'fail',
                    'message': 'Invalid auth token header format.'
                }
                return make_response(jsonify(responseObject)), 401

            # Validate the auth token
            if auth_token:
                resp = User.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    # JWT Token is valid, continue:
                    if (return_user_id):
                        return f(*args, **kwargs, user_id=resp)
                    return f(*args, **kwargs)
                responseObject = {
                    'status': 'fail',
                    'message': resp
                }
                return make_response(jsonify(responseObject)), 401
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return make_response(jsonify(responseObject)), 401
        return decorated_function
    return decorator

# Use this if you want to use the wrapper method of applying decorators to pluggable views.
# http://stackoverflow.com/questions/31397842/decorating-flask-pluggable-views-builderror
# TODO: Delete this as this is really just redundant code meant for documentation.
def jwt_wrapper(f, return_user_id=False):
    """JWT Auth Decorator"""
    def decorator(*args, **kwargs):
        # get the auth token
        try:
            auth_header = request.headers.get('Authorization')
            if auth_header:
                auth_token = auth_header.split(" ")[1]
            else:
                auth_token = ''
        except Exception as e:
            # Failed to get the auth token. Could be formatting, etc.
            responseObject = {
                'status': 'fail',
                'message': 'Invalid auth token header format.'
            }
            return make_response(jsonify(responseObject)), 401

        # Validate the auth token
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # JWT Token is valid, continue:
                if (return_user_id):
                    return f(*args, **kwargs, user_id=resp)
                return f(*args, **kwargs)
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401
    return decorator