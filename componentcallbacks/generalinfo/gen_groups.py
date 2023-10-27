

import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html, callback


layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div("Welfare alerts(in groups)"), width=8),
                dbc.Col(html.Div("5"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Nutrition alerts"), width=8),
                dbc.Col(html.Div("0"), width=2),
            ],justify="between",
            ),
        
    ]
)

