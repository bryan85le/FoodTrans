#https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
from dash import Input, Output, dcc, html, callback, register_page, dash_table
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np


data = px.data.gapminder()
PAGE_SIZE = 10

layout = dmc.Container(
    [
                dash_table.DataTable(
                    data.to_dict("records"),
                    [{"name": i, "id": i} for i in data.columns],
                    id='tbl',
                    page_current=0,
                    page_size=PAGE_SIZE,
                    style_table={'overflowX': 'auto'},
                    fixed_columns={'headers': True, 'data': 2},
                ),
    ],
    fluid=True,
)

