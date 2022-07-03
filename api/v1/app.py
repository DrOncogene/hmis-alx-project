#!/usr/bin/python3
""" Flask Application """
from os import environ

from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask, jsonify, make_response
from flask_cors import CORS

from storage import storage
from api.v1.views import app_views

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(e):
    """ Close Storage """
    storage.close()


@app.errorhandler(400)
def bad_request(e):
    """
    400 error handler
    ---
    responses:
      400:
        description: invalid request
    """
    return make_response(jsonify(error=str(e)), 400)


@app.errorhandler(404)
def not_found(e):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify(error=str(e)), 404)

app.config['SWAGGER'] = {
    'title': 'HMIS Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    HOST = environ.get('HMIS_API_HOST')
    PORT = environ.get('HMIS_API_PORT')
    if not HOST:
        HOST = '0.0.0.0'
    if not PORT:
        PORT = '5000'
    app.run(host=HOST, port=PORT, threaded=True)
