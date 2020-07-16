# app/__init.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_type):    #dev, test, prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type+'.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)    #bind the database to Flask app
    bootstrap.init_app(app)     #Initialize bootstrap

    from app.catalog import main    #import blueprint
    app.register_blueprint(main)    #register blueprint

    return app

