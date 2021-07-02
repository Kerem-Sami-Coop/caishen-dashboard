from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

__version__ = "0.0.0"

bootstrap = Bootstrap()
# db = SQLAlchemy()
# migrate = Migrate()
# lm = LoginManager()
# lm.login_view = "auth.login"



def create_app(config_class=Config):
    server = Flask("caishen")
    # configuration
    server.config.from_object(config_class)

    # register extensions
    # db.init_app(server)
    # migrate.init_app(server, db)
    bootstrap.init_app(server)

    with server.app_context():

        # register blueprints
        from caishen_dashboard.server import bp as bp_main
        server.register_blueprint(bp_main)
        from caishen_dashboard.stock_app import bp as bp_dashapps
        server.register_blueprint(bp_dashapps)

        # process dash apps
        # dash app 1: Stock graphs
        from caishen_dashboard.stock_app.main import add_dash as ad1
        server = ad1(server)

        return server
