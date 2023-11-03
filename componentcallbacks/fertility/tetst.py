# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dash_table, dcc, html, register_page

df = pd.read_csv("data/general.csv")
df = df.loc[[2], "num_lact":"daily_avg_yeild"]
df = df.rename(
    columns={
        "num_lact": "Number Lactation",
        "num_Insem": "Number Insemation",
        "daily_avg_yeild": "Daily Average Yeild",
        "age": "Age (Months)",
        "DIM": "DIM",
    }
)


data = pd.melt(df)
data = data.rename(columns={"variable": "Yeild", "value": "Information"})


layout = dbc.Card(
    dbc.CardBody(
        [
            dash_table.DataTable(
                data=data.to_dict("records"),
                columns=[{"name": i, "id": i} for i in data.columns],
                id="insemi_tbl",
                style_table={"overflowX": "auto"},
            ),
            dbc.Alert(id="semi_tbl_out"),
        ]
    )
)


@callback(
    Output("semi_tbl_out", "children"),
    Input("tbl", "active_cell"),
)
def update_alerts(active_cell):
    return active_cell["column_id"]
