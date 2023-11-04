# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dash_table, dcc, html, register_page

PAGE_SIZE = 10

layout = dmc.Container(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    dash_table.DataTable(id="tbl"),
                ]
            )
        )
    ],
    fluid=True,
)


@callback(Output("tbl", "data"), Input("global-data", "data"))
def fereport(data):
    df = pd.DataFrame.from_dict(data)

    df = df.loc[:, "index":"group"]


    return df.to_dict("records")
