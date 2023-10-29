

import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html, callback, dcc

import plotly.express as px

df = px.data.tips()
fig = px.pie(df, values='tip', names='day')

layout = dbc.Container([
    dbc.Row(
            [
                dbc.Col(html.H3('Animal Inventory'), width=8),
                dbc.Col(html.Div("Cows"), width=2),
                dbc.Col(html.Div("Heifers"), width=2),
            ],justify="between",
            ),
    html.Hr(),
        dbc.Row(
            [
                dbc.Col(html.Div("Cows"), width=8),
                dbc.Col(html.Div("1094"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Pregnant Milk"), width=8),
                dbc.Col(html.Div("315"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Open"), width=8),
                dbc.Col(html.Div("653"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Dry"), width=8),
                dbc.Col(html.Div("126"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            dcc.Graph(figure=fig),justify="between",
            ),
])

