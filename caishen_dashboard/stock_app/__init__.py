from flask import Blueprint

bp = Blueprint("stock_app", __name__, template_folder="templates")

from caishen_dashboard.stock_app import routes  # noqa:F401
