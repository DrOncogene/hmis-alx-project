#!/usr/bin/python3
"""app config vars"""
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """sets general config vars"""
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    JSONIFY_PRETTYPRINT_REGULAR = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"
    SWAGGER = {
        'title': 'HMIS Restful API',
        'uiversion': 3
    }


class ProdConfig(Config):
    """set production config"""
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False


class DevConfig(Config):
    """set development config"""
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True
