

import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html, callback

layout = dbc.Container([
    html.H3('Fertility'),
    html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div("Animals to bread"), width=8),
                dbc.Col(html.Div("8"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Suspected abortion"), width=8),
                dbc.Col(html.Div("1"), width=2),
            ],justify="between",
            ),
])
