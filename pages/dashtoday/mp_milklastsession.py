# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dash_table, dcc, html, register_page
from dash.exceptions import PreventUpdate

from componentcallbacks import Milkproduction

register_page(__name__, path="/milklastsession", title="Milk last session")


layout = html.Div(
    [
        Milkproduction(),
    ]
)
