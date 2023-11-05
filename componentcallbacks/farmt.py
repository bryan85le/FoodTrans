import random
import uuid
from typing import Optional

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
from dash import MATCH, Input, Output, callback, dash_table, dcc, html
from dash.development.base_component import Component
from dash_bootstrap_components import Container


class tlbContent(html.Div):
    class ids:
        title = lambda aio_id: {"component": "tbl-title", "aio_id": aio_id}
        value = lambda aio_id: {"component": "tbl-value", "aio_id": aio_id}

    ids = ids

    def __init__(
        self,
        id: Optional[str] = None,
    ):
        id = id or str(uuid.uuid4())

        super().__init__(id=id, children=self.show(id))

    def show(self, id) -> html.Div:
        return [
            html.Div(
                children=dmc.SimpleGrid(
                    cols=2,
                    children=[
                        dbc.Col(
                            dmc.Stack(
                                [
                                    dmc.Anchor(href="", id=self.ids.title(id)),
                                ],
                                align="flex-start",
                                justify="center",
                            )
                        ),
                        dbc.Col(
                            dmc.Stack(
                                [
                                    dmc.TextInput(
                                        style={"width": 70, "textAlign": "center"},
                                        # value="123",
                                        disabled=True,
                                        id=self.ids.value(id),
                                    ),
                                ],
                                align="flex-end",
                                justify="center",
                            )
                        ),
                    ],
                ),
            )
        ]

    @callback(
        Output(ids.value(MATCH), "value"),
        Output(ids.title(MATCH), "children"),
        Output(ids.title(MATCH), "href"),
        Input("global-data", "data"),
    )
    def feeddata(data):
        df = pd.DataFrame.from_dict(data)
        df = df.loc[:, "index":"group"]
        df.to_dict("records")

        return random.randrange(50, 100, 5), "Milk Production", "/none"


class Health(html.Div):
    """Container report.

    Parameters
    ----------
    id : str, default='health-report'
        Dashboard ID.
    """

    def __init__(
        self,
        id: Optional[str] = None,
    ):
        id = id or str(uuid.uuid4())

        super().__init__(
            id=id,
            children=self.health_report(),
        )

    # Create layout for Fertilityy Report
    def health_report(self) -> dbc.Card:
        return [
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/log.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("To do Today"),
                            tlbContent(),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/log.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Health"),
                            tlbContent(),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
        ]
