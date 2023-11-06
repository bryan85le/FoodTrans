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
    Patch,
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
                        ]
                    ),
                ],
            ),
        ]

    @callback(Output("dynamic-dropdown-container-div", "children"), Input("global-data", "data"))
    def milklastsessiontable(data):
        id = str(uuid.uuid4())
        df = pd.DataFrame.from_dict(data)

        df = df.loc[:, "index":"group"]
        df.to_dict("records")

        patched_children = Patch()
        new_element = html.Div(
            [
                dash_table.DataTable(id={"type": "table-content", "id": id}, data=df.to_dict("records")),
                dbc.Alert(id={"type": "table-alert", "id": id}),
                dcc.Dropdown(["Alert", "Graph"], id={"type": "table-dropdown", "id": id}),
                dbc.Alert(id={"type": "table-alert_drop", "id": id}),
            ]
        )

        patched_children.append(new_element)
        return patched_children

    @callback(
        Output({"type": "table-alert", "id": MATCH}, "children"),
        Input({"type": "table-content", "id": MATCH}, "active_cell"),
    )
    def display_output(active_cell):
        return str(active_cell)
