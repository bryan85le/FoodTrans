#https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
from dash import Input, Output, dcc, html, callback, register_page, dash_table
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np


data = px.data.gapminder()



layout = dmc.Container(
    [
        dcc.Graph(id="graph"),
        dbc.Alert(id='tbl_out'),

    ],
    fluid=True,
)



@callback(
    Output("graph", "figure"),
    Output('tbl_out', 'children'),
    Input('tbl', 'active_cell'),
    Input('tbl', "page_current"),
    Input('tbl', "page_size")
    )
def update_line_chart(active_cell, page_current, page_size):
    df = px.data.gapminder() # replace with your own data source
    rw = active_cell['row']
    row = page_current*page_size + rw
    cownum = np.array([df.at[row,'continent']])

    mask = df.continent.isin(cownum)
    fig = px.line(df[mask], 
        x="year", y="lifeExp", color='country')
    return fig, cownum


