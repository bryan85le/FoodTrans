

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
                dbc.Col(html.Div("To dry today"), width=8),
                dbc.Col(html.Div("56"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Due calving"), width=8),
                dbc.Col(html.Div("26"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Sorted cows"), width=8),
                dbc.Col(html.Div("13"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("For prenancy check"), width=8),
                dbc.Col(html.Div("34"), width=2),
            ],justify="between",
            ),
    ]
)

