from flask import Flask, g
from hf1.database import db
from hf1.bp_main import bp_main
from hf1.bp_products import bp_products
from hf1.bp_account import bp_account
from hf1 import cli
import datetime

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    uri='sqlite:///%s/%s.db' % (app.instance_path , __name__ )
    app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS='false',
        SQLALCHEMY_DATABASE_URI=uri,
        SECRET_KEY='DEV',
        APP_VERSION='set APP_VERSION in instance config')

    app.config.from_pyfile('config.cfg', silent=False)

    db.init_app(app)
    init_app(app)

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_account)

    return app

def before_request():
    g.year = datetime.datetime.now().year

def init_app(app):
    cli.init_cli_commands(app)
    app.before_request(before_request)