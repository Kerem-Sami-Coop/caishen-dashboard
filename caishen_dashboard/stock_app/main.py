from dash import Dash
import dash_bootstrap_components as dbc
from caishen_dashboard.stock_app.callbacks import register_callback
from caishen_dashboard.stock_app.layout import graph_layout
from caishen_dashboard.auth.utils import login_required
import pandas as pd


APP_ID = "stock"
URL_BASE = f"/{APP_ID}/"
MIN_HEIGHT = 200


# def _protect_dashviews(dashapp):
#     for view_func in dashapp.server.view_functions:
#         if view_func.startswith(dashapp.config.url_base_pathname):
#             dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])


def add_dash(server, protect=True):

    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
    ]

    app = Dash(
        server=server,
        url_base_pathname=URL_BASE,
        suppress_callback_exceptions=True,
        external_stylesheets=external_stylesheets
    )

    data_source = "https://raw.githubusercontent.com/plotly/datasets/master/dash-stock-ticker-demo.csv"
    df = pd.read_csv(data_source, index_col=False)
    df.drop(df.columns[0], inplace=True, axis=1)

    app.layout = dbc.Container([
        graph_layout(df, "Stock")
    ])

    register_callback(app)

    # if protect:
    #     _protect_dashviews(app)

    return server
