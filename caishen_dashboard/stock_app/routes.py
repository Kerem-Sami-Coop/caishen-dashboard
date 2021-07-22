from flask import render_template
from caishen_dashboard.stock_app import bp
from caishen_dashboard.stock_app import main as stock
from caishen_dashboard.auth.utils import login_required


@bp.route("/stock")
@login_required
def stock_dash_app():
    return render_template("stock_app/dash_app.html", dash_url=stock.URL_BASE, min_height=stock.MIN_HEIGHT)
