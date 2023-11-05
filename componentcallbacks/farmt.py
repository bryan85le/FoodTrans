import random
import uuid
from typing import Optional

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
from dash import Input, Output, callback, dash_table, dcc, html
from dash.development.base_component import Component
from dash_bootstrap_components import Container


class Farmtoday(Container):
    """Container Farm Today report.

    Parameters
    ----------
    id : str, default='farm-today-report-id'
        Dashboard ID.
    className : str, default='arm-today-report-css'
    """

    def __init__(
        self,
        id: str = "farm-today-report-id",
        className: str = "farm-today-report-css",
    ):
        super().__init__(
            id=id,
            fluid=True,
            children=self.ferttable(),
            className=className,
        )

    # Creat layout variable
    milkls = dmc.Grid(
        children=[
            dmc.Col(
                html.Div(
                    [
                        dmc.Stack(
                            [
                                dmc.Anchor(
                                    "Milk last session",
                                    href="/none",
                                ),
                                dmc.Anchor(
                                    "Milk previous day",
                                    href="/none",
                                ),
                                dmc.Anchor(
                                    "Cows milked last session",
                                    href="/none",
                                ),
                                dmc.Anchor(
                                    "Last 24H average milk per cow",
                                    href="/none",
                                ),
                                dmc.Anchor(
                                    "Fat % last 24H",
                                    href="/none",
                                ),
                                dmc.Anchor(
                                    "Protein % last 24H",
                                    href="/none",
                                ),
                            ],
                            align="flex-start",
                            justify="center",
                        )
                    ]
                ),
                span="auto",
                style={
                    # "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                    # "textAlign": "center",
                },
            ),
            dmc.Col(
                html.Div(
                    [
                        dmc.Stack(
                            [
                                dmc.TextInput(
                                    style={"width": 70, "textAlign": "center"},
                                    placeholder="1284",
                                    disabled=True,
                                ),
                                dmc.TextInput(
                                    style={"width": 70, "textAlign": "center"},
                                    placeholder="2764",
                                    disabled=True,
                                ),
                                dmc.TextInput(
                                    style={"width": 70, "textAlign": "center"},
                                    placeholder="67",
                                    disabled=True,
                                ),
                                dmc.TextInput(
                                    style={"width": 70, "textAlign": "center"},
                                    placeholder="40.1",
                                    disabled=True,
                                ),
                                dmc.TextInput(
                                    style={"width": 70, "textAlign": "center"},
                                    placeholder="3.65%",
                                    disabled=True,
                                ),
                                dmc.TextInput(
                                    style={"width": 70, "textAlign": "center"},
                                    placeholder="3.28%",
                                    disabled=True,
                                ),
                            ],
                            align="flex-end",
                            justify="center",
                        )
                    ]
                ),
                span=4,
                style={
                    # "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                    # "textAlign": "center",
                },
            ),
        ],
        align="center",
        style={
            "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
            # "textAlign": "center",
        },
        # gutter="xl",
    )

    # Create layout for Fertilityy Report
    def ferttable(self) -> dbc.Card:
        return [
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/log.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("To do Today"),
                            self.milkls,
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card([dbc.CardBody([])]),
        ]

    @callback(Output("tbl-farm-report", "data"), Input("global-data", "data"))
    def fereport(data):
        df = pd.DataFrame.from_dict(data)
        df = df.loc[:, "index":"group"]

        return df.to_dict("records")


class update(html.Div):
    def __init__(
        self,
        id: Optional[str] = None,
    ):
        id = id or str(uuid.uuid4())

        super().__init__(id=id, children=self.showvalue())

    def showvalue(self) -> html.Div:
        return [
            html.Div(
                children=dmc.SimpleGrid(
                    cols=2,
                    children=[
                        dbc.Col(
                            html.Div("Tittle"),
                        ),
                        dbc.Col(
                            html.Div("Value"),
                        ),
                    ],
                ),
            )
        ]


class subcontent(dmc.Grid):
    """Default box."""

    def __init__(
        self,
        id: str = "subcontent-id",
        title: Optional[str] = None,
        link: Optional[str] = None,
    ):
        super().__init__(
            id=id,
            children=[self.title(title, link), self.content(id)],
        )

    # Create layout for Fertilityy Report
    def title(self, title, link) -> html.Div:
        return html.Div(
            [
                dmc.Col(
                    dmc.Stack(
                        [
                            dmc.Anchor(
                                children=title,
                                href=link,
                            ),
                        ],
                        align="flex-start",
                        justify="center",
                    ),
                    span="auto",
                    style={
                        "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                        # "textAlign": "center",
                    },
                ),
            ]
        )

    # Create layout for Fertilityy Report
    def content(self, id) -> html.Div:
        return html.Div(
            [
                dmc.Col(
                    dmc.Stack(
                        [
                            dmc.TextInput(
                                style={"width": 70, "textAlign": "center"},
                                placeholder="3.28%",
                                disabled=True,
                                id=f"{id}--value",
                            ),
                        ],
                        align="flex-start",
                        justify="center",
                    ),
                    span=12,
                    style={
                        "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                        # "textAlign": "center",
                    },
                    offset=10,
                ),
            ]
        )

    @callback(Output("tbl-farm-report1", "data"), Input("global-data", "data"))
    def fereport(data):
        df = pd.DataFrame.from_dict(data)
        df = df.loc[:, "index":"group"]

        return df.to_dict("records")


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
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            # subcontent(title="Milk ddd", link="/none"),
                            update(id="update-id")
                        ]
                    )
                ]
            ),
        ]
