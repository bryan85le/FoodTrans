import datetime
import random
import uuid
from typing import Optional

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import (
    ALL,
    ALLSMALLER,
    MATCH,
    Input,
    Output,
    State,
    callback,
    dash_table,
    dcc,
    html,
)
from dash.development.base_component import Component
from dash_bootstrap_components import Container

from .functions import tlbContent


class Milkproduction(Container):
    """Container report.

    Parameters
    ----------
    id : str, default='health-report'
        Dashboard ID.
    """

    class ids:
        table = lambda aio_id: {"component": "tbl-content", "aio_id": aio_id}
        cowcell = lambda aio_id: {"component": "cowcell-content", "aio_id": aio_id}

    ids = ids

    df = px.data.tips()
    fig = px.pie(df, values="tip", names="day")
    PAGE_SIZE = 10

    def __init__(
        self,
        id: Optional[str] = None,
    ):
        id = id or str(uuid.uuid4())

        super().__init__(
            id=id,
            children=self.milkproduction_report(id),
        )

    # Create layout for Fertilityy Report
    def milkproduction_report(self, id) -> dbc.Card:
        imagestyle = {"width": "8rem"}
        return [
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/production_&_milk_quality.jpg", top=True, style=imagestyle),
                    dbc.CardBody(
                        [
                            html.H3("Milk last session"),
                            html.Div(id="dynamic-dropdown-container-div", children=[]),
                            dash_table.DataTable(id=self.ids.table(id)),
                        ]
                    ),
                ],
            ),
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/milking_efficiency.jpg", top=True, style=imagestyle),
                    dbc.CardBody(
                        [
                            html.H3("Animals Invetory"),
                            dcc.Dropdown(["Alert", "Graph"], id="loading-states-table-prop"),
                            dbc.Alert(id="semi_tbl_out"),
                            dcc.Graph(figure=self.fig),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
        ]

    @callback(Output(ids.table(MATCH), "data"), Input("global-data", "data"))
    def milklastsessiontable(data):
        df = pd.DataFrame.from_dict(data)

        df = df.loc[:, "index":"group"]

        return df.to_dict("records")

    @callback(
        Output("semi_tbl_out", "children"),
        Input("loading-states-table-prop", "value"),
        Input(ids.table(ALL), "active_cell"),
        Input(ids.table(ALL), "page_current"),
        Input(ids.table(ALL), "page_size"),
    )
    def showcell(value, active_cell, page_current, page_size):
        return str(active_cell)
