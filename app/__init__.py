#!/usr/bin/env python
#coding=utf-8

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

mail = Mail()
db = SQLAlchemy()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .api_1 import api_bp as api_1_blueprint
    app.register_blueprint(api_1_blueprint, url_prefix='/api/v1')

    return app
