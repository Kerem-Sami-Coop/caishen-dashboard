import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    BRAND = os.environ.get("BRAND") or "My Brand"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super_duper_secret"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "db/users.db")
    SQLALCHEMY_BINDS = {
        "my_data": os.environ.get("SQLALCHEMY_BIND_MY_DATA") or "sqlite:///" + os.path.join(basedir, "db/my_data.db")
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
