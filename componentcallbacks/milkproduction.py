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
        table = lambda aio_id: {"type": "alltbl-table", "aio_id": aio_id}
        alert = lambda aio_id: {"type": "tbl-alert", "aio_id": aio_id}
        htmlshow = lambda aio_id: {"type": "tbl-html-show", "aio_id": aio_id}
        dropdown = lambda aio_id: {"type": "tbl-dropdown", "aio_id": aio_id}
        htmldropdown = lambda aio_id: {"type": "tbl-html-dropdown", "aio_id": aio_id}
        alert1 = lambda aio_id: {"type": "tbl-alert1", "aio_id": aio_id}

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
            children=self.milkproduction_report(),
        )

    """
    Description:
        1. Milk production content
    
    """

    def milkproduction_report(self) -> dbc.Card:
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

    """
    Description:
        1. Feed for a table
    
    """

    @callback(Output("dynamic-dropdown-container-div", "children"), Input("global-data", "data"))
    def milklastsessiontable(data):
        df = pd.DataFrame.from_dict(data)

        df = df.loc[:, "index":"group"]
        df.to_dict("records")

        patched_children = Patch()

        patched_children.append(
            html.Div(
                [
                    dash_table.DataTable(id=Milkproduction.ids.table(f"{id}"), data=df.to_dict("records")),
                    dbc.Alert(id=Milkproduction.ids.alert(f"{id}")),
                    html.Div(
                        id=Milkproduction.ids.htmlshow(f"{id}"),
                        children=[],
                    ),
                ]
            )
        )
        return patched_children

    """
    Description:
        1. Show a detail information of table cell
    
    """

    @callback(
        Output(ids.alert(MATCH), "children"),
        Input(ids.table(MATCH), "active_cell"),
    )
    def display_output(active_cell):
        return str(active_cell)

    """
    Description:
        1. Show a detail information of table cell
    
    """

    def showtdropdown() -> html.Div:
        return html.Div(
            [
                dcc.Dropdown(["Alert", "Graph"], id=Milkproduction.ids.dropdown(f"{id}")),
                html.Div(
                    id=Milkproduction.ids.htmldropdown(f"{id}"),
                ),
            ]
        )

    @callback(
        Output(ids.htmlshow(MATCH), "children"),
        Input(ids.table(MATCH), "active_cell"),
        prevent_initial_call=True,
    )
    def html_show(active_cell):
        return Milkproduction.showtdropdown()

    """
    Description:
        1. Show a detail information of table cell
    

    """

    def showtablecell() -> html.Div:
        return [tlbContent(title="Hello Viet nam"), tlbContent(title="Hello Viet nam Muon nam")]

    @callback(
        Output(ids.htmldropdown(MATCH), "children"),
        Input(ids.dropdown(MATCH), "value"),
        prevent_initial_call=True,
    )
    def html_show_drop(value):
        return Milkproduction.showtablecell()
