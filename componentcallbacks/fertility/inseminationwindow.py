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
                    data=data.to_dict("records"),
                    columns=[{"name": i, "id": i} for i in data.columns],
                    id='insemination-tbl',
                    page_current=0,
                    page_size=PAGE_SIZE,
                    style_table={'overflowX': 'auto'},
                    fixed_columns={'headers': True, 'data': 2},
                ),
                dbc.Alert(id='semi_tbl_out'),
    ],
    fluid=True,
)


@callback(
    Output('semi_tbl_out', 'children'),
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
    return cownum


