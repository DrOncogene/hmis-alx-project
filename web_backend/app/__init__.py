#!/usr/bin/python3
"""module to define the application factory"""
from flask import Flask, jsonify
from flask_cors import CORS

from storage import storage
from .api.v1.views import api_views
from .auth.views import auth_views


cors = CORS()


def make_app():
    """initializes the application object"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('web_backend.config.DevConfig')
    from .api import swagger
    from .auth import login_manager

    login_manager.init_app(app)
    cors.init_app(app, resources={r"/api/v1/*": {"origins": "*"},
                  r"/auth/*": {"origins": "*"}})
    swagger.init_app(app)

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
        return jsonify(error=str(e)), 400

    @app.errorhandler(404)
    def not_found(e):
        """ 404 Error
        ---
        responses:
        404:
            description: a resource was not found
        """
        return jsonify(error=str(e)), 404

    @app.errorhandler(401)
    def not_priviledged(e):
        return jsonify({"401 error": str(e).split(':')[1]}), 401

    with app.app_context():
        app.register_blueprint(api_views)
        app.register_blueprint(auth_views)

        return app
