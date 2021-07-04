from flask import render_template
from caishen_dashboard.stock_app import bp
from caishen_dashboard.stock_app import main as stock


@bp.route("/stock")
def stock_dash_app():
    return render_template("stock_app/dash_app.html", dash_url=stock.URL_BASE, min_height=stock.MIN_HEIGHT)
