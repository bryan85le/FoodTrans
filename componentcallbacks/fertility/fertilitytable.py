# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dash_table, dcc, html, register_page

df = pd.read_csv("data/general.csv")
data = df.loc[:, "Index":"cow_sign"]
data = data.rename(
    columns={
        "Index": "Index",
        "days": "Last Days",
        "cowid": "Code ID",
        "cowname": "Name",
        "status": "Status",
        "Groups": "Groups",
        "cow_yeild": "Cow Yeild",
        "cow_sign": "Cow Sign",
    }
)


PAGE_SIZE = 10

layout = dmc.Container(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    dash_table.DataTable(
                        data.to_dict("records"),
                        [{"name": i, "id": i} for i in data.columns],
                        id="tbl",
                        page_current=0,
                        page_size=PAGE_SIZE,
                        style_table={"overflowX": "auto"},
                        fixed_columns={"headers": True, "data": 2},
                    ),
                ]
            )
        )
    ],
    fluid=True,
)
