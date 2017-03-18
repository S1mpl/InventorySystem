from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from app.login import login as login_blueprint
    from app.datacenters import datacenters as datacenters_blueprint
    from app.servers import servers as servers_blueprint
    app.register_blueprint(login_blueprint)
    app.register_blueprint(datacenters_blueprint)
    app.register_blueprint(servers_blueprint)

    return app