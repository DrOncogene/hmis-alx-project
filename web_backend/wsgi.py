#!/usr/bin/python3
"""provides the wsgi entry point"""
from os import environ
from .app import make_app


app = make_app()


if __name__ == "__main__":
    HOST = environ.get('HMIS_API_HOST')
    PORT = environ.get('HMIS_API_PORT')
    if not HOST:
        HOST = '0.0.0.0'
    if not PORT:
        PORT = '5000'
    app.run(host=HOST, port=PORT, threaded=True)
