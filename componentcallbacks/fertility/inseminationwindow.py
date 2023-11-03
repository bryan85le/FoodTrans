# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
from random import randint, seed
from time import sleep

import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dash_table, dcc, html
from dash.exceptions import PreventUpdate

# For the documentation to always render the same values
seed(0)
# data = data.loc[data['continent'] == 'Europe', ['country', 'year']]

layout = html.Div(
    [
        "Choose property to load: ",
        dcc.Dropdown(["style_cell", "data"], id="loading-states-table-prop"),
        html.Br(),
        dash_table.DataTable(id="loading-states-table"),
        dbc.Alert(id="semi_tbl_out"),
    ]
)


@callback(Output("loading-states-table", "style_cell"), Input("loading-states-table-prop", "value"))
def loading_style_cell(value):
    if value == "style_cell":
        # sleep(5)
        return {
            "color": "rgb({}, {}, {})".format(randint(0, 255), randint(0, 255), randint(0, 255))
        }
    raise PreventUpdate


@callback(
    Output("loading-states-table", "data"),
    Output("semi_tbl_out", "children"),
    Input("loading-states-table-prop", "value"),
    Input("tbl", "active_cell"),
)
def loading_data(value, active_cell):
    if value == "data":
        df = pd.read_csv("data/general.csv")
        row = active_cell["row"]
        cowid = np.array([df.at[row, "cowid"]])

        mask = df.cowid.isin(cowid)
        df = df[mask]
        df = df.loc[:, "num_lact":"daily_avg_yeild"]

        return df.to_dict("records"), cowid
    raise PreventUpdate
