from dash import Dash
import dash_bootstrap_components as dbc
from caishen_dashboard.stock_app.callbacks import register_callback
from caishen_dashboard.stock_app.layout import graph_layout
import pandas as pd


APP_ID = "stock"
URL_BASE = f"/{APP_ID}/"
MIN_HEIGHT = 200


def add_dash(server):

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

    return server
