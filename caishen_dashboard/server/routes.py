from flask import render_template
from caishen_dashboard.server import bp


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("server/index.html")
