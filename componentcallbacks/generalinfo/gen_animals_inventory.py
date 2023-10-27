

import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html, callback, dcc

import plotly.express as px

df = px.data.tips()
fig = px.pie(df, values='tip', names='day')

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div("Animal Invetory"), width=8),
                dbc.Col(html.Div("8"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Cows"), width=8),
                dbc.Col(html.Div("325"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            dcc.Graph(figure=fig),justify="between",
            ),
        
    ]
)

