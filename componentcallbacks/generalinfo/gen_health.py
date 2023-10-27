

import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html, callback


layout = dbc.Container([
    html.H3('General health'),
    html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div("Mastitis"), width=8),
                dbc.Col(html.Div("1"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Digestion Problems"), width=8),
                dbc.Col(html.Div("1"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Ketosis"), width=8),
                dbc.Col(html.Div("4"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Fresh cows to check"), width=8),
                dbc.Col(html.Div("17"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Anestrus"), width=8),
                dbc.Col(html.Div("15"), width=2),
            ],justify="between",
            ),
])
