#https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
from dash import Input, Output, dcc, html, callback, register_page, dash_table
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from componentcallbacks.fertility import (
                                            fertilitytable as fe,
                                            graphreport as gr,
                                            )

register_page(
    __name__,
    path = '/ane',
    title = 'Anestrus report'
)


layout = html.Div(
    [
        dmc.Title('Anestrus Report'),
        dmc.Space(h=20),
        fe.layout,
        gr.layout,
    ]
)





