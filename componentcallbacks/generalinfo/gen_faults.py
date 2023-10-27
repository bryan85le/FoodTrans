

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
                dbc.Col(html.Div("Un-Assigned Tags"), width=8),
                dbc.Col(html.Div("15"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Not Identified"), width=8),
                dbc.Col(html.Div("-"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("in Milking"), width=8),
                dbc.Col(html.Div("1"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Wrong Group"), width=8),
                dbc.Col(html.Div("1"), width=2),
            ],justify="between",
            ),
    ]
)

