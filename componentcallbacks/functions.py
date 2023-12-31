import datetime
import random
import uuid
from typing import Optional

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
from dash import MATCH, Input, Output, State, callback, dash_table, dcc, html
from dash.development.base_component import Component
from dash_bootstrap_components import Container


class tlbContent(html.Div):
    class ids:
        title = lambda aio_id: {"component": "tbl-title", "aio_id": aio_id}
        value = lambda aio_id: {"component": "tbl-value", "aio_id": aio_id}

    ids = ids

    def __init__(
        self,
        title: Optional[str] = None,
        href: str = "#",
        value: str = "",
        id: Optional[str] = None,
    ):
        id = id or str(uuid.uuid4())
        href = href
        title = title
        value = value

        super().__init__(id=id, children=self.show(id, title, href))

    def show(self, id, title, href) -> html.Div:
        return [
            html.Div(
                children=dmc.SimpleGrid(
                    cols=2,
                    children=[
                        dbc.Col(
                            dmc.Stack(
                                [
                                    dmc.Anchor(children=title, href=href, id=self.ids.title(id)),
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
                            ), align="center"

                        ),
                    ],
                ),
            )
        ]

    @callback(
        Output(ids.value(MATCH), "value"),
        Output(ids.title(MATCH), "href"),
        State(ids.title(MATCH), "href"),
        Input("global-data", "data"),
        Input("interval-component", "n_intervals"),
    )
    def feeddata(href, data, _):
        df = pd.DataFrame.from_dict(data)
        df = df.loc[:, "index":"group"]
        df.to_dict("records")

        return (random.randrange(50, 100, 5), href)
