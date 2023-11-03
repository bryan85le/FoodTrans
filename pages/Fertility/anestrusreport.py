#https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import collections

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dash_table, dcc, html, register_page
from dash.exceptions import PreventUpdate

from componentcallbacks.fertility import fertilityreport as fer
from componentcallbacks.fertility import fertilitytable as fet

register_page(
    __name__,
    path = '/ane',
    title = 'Anestrus report'
)


layout = html.Div(
    [

        dmc.Title('Anestrus Report'),
        dmc.Space(h=20),
        fet.layout,
        fer.layout,

    ]
)


