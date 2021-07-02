from flask import Blueprint

bp = Blueprint("server", __name__, template_folder="templates")

from caishen_dashboard.server import routes  # noqa:F401
