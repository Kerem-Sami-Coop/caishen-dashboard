import dash_html_components as html
from dash_core_components import Graph
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from caishen_stonks.technical_indicators import bollinger_bands
import colorlover as cl
import pandas as pd

COLORSCALE = cl.scales["9"]["qual"]["Paired"]


def register_callback(dashapp):
    @dashapp.callback(
        Output(component_id="graphs", component_property="children"),
        Input(component_id="stock-ticker-input", component_property="value"),
        State(component_id="df-store", component_property="data"))
    def update_graph(tickers, data):
        if tickers is None:
            raise PreventUpdate
        graphs = []

        if not tickers:
            graphs.append(html.H3(
                "Select a stock ticker.",
                style={"marginTop": 20, "marginBottom": 20}
            ))
        else:
            df = pd.DataFrame(data)
            for i, ticker in enumerate(tickers):
                subset = df[df["Stock"] == ticker].sort_values(by="Date")

                candlestick = {
                    "x": subset["Date"].values,
                    "open": subset["Open"].values,
                    "high": subset["High"].values,
                    "low": subset["Low"].values,
                    "close": subset["Close"].values,
                    "type": "candlestick",
                    "name": ticker,
                    "legendgroup": ticker,
                    "increasing": {"line": {"color": COLORSCALE[0]}},
                    "decreasing": {"line": {"color": COLORSCALE[1]}}
                }
                bb_bands = bollinger_bands(subset["Close"].values)
                exclude = bb_bands[0].count(-1)
                bollinger_traces = [{
                    "x": subset["Date"].values[exclude:],
                    "y": y[exclude:],
                    "type": "scatter", "mode": "lines",
                    "line": {"width": 1, "color": COLORSCALE[(i * 2) % len(COLORSCALE)]},
                    "hoverinfo": "none",
                    "legendgroup": ticker,
                    "showlegend": True if i == 0 else False,
                    "name": "{} - bollinger bands".format(ticker)
                } for i, y in enumerate(bb_bands)]
                graphs.append(Graph(
                    id=ticker,
                    figure={
                        "data": [candlestick] + bollinger_traces,
                        "layout": {
                            "margin": {"b": 0, "r": 10, "l": 60, "t": 0},
                            "legend": {"x": 0}
                        }
                    }
                ))

        return graphs
