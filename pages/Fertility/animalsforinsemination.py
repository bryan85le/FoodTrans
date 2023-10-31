#https://www.afimilk.com/docs/documents/afifarm/animals%20for%20insemination.htm?tocpath=_____1
from dash import Input, Output, dcc, html, callback, register_page, dash_table
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from componentcallbacks.fertility import (
                                            #fertilityreport as fe,
                                            graphreport as gr,
                                            )
#data = px.data.stocks()

register_page(
    __name__,
    path = '/semi',
    title = 'Animals for Insemination'
)


layout = html.Div(
    [
        dmc.Title('Anestrus Report'),
        dmc.Space(h=20),
        #fe.layout,
        gr.layout,
    ]
)