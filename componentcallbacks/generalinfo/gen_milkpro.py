

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
                dbc.Col(html.Div("Milk last session"), width=8),
                dbc.Col(html.Div("1284"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Milk previous day"), width=8),
                dbc.Col(html.Div("2764"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Cows milked last session"), width=8),
                dbc.Col(html.Div("67"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Last 24H average milk per cow"), width=8),
                dbc.Col(html.Div("40.1"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Fat % last 24H"), width=8),
                dbc.Col(html.Div("3.65%"), width=2),
            ],justify="between",
            ),
        dbc.Row(
            [
                dbc.Col(html.Div("Protein % last 24H"), width=8),
                dbc.Col(html.Div("3.28"), width=2),
            ],justify="between",
            ),
    ]
)

