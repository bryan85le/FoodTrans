# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dash_table, dcc, html, register_page

# data = px.data.gapminder()
# df = pd.DataFrame(data)
# df.to_csv('data/10days.csv')

data = pd.read_csv("data/10days.csv")


layout = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(id="graph"),
        ]
    )
)


@callback(
    Output("graph", "figure"),
    [State("collapse1", "is_open")],
    Input("tbl", "active_cell"),
    Input("tbl", "page_current"),
    Input("tbl", "page_size"),
)
def update_line_chart(is_open1, active_cell, page_current, page_size):
    if is_open1 and active_cell:
        df = px.data.gapminder()  # replace with your own data source
        rw = active_cell["row"]
        row = page_current * page_size + rw
        cownum = np.array([df.at[row, "continent"]])

        mask = df.continent.isin(cownum)
        fig = px.line(df[mask], x="year", y="lifeExp", color="country")
        return fig
    return fig
