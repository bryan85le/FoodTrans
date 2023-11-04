from typing import Optional

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
from dash import Input, Output, callback, dash_table, dcc, html
from dash.development.base_component import Component
from dash_bootstrap_components import Container


class Farmtoday(Container):
    """Container principal da aplicação.

    Parameters
    ----------
    children : Dash component | list of Dash components, optional
        The container main content.
    navbar : dash_charlotte.Navbar, optional
        Navbar added at the top of the dashboard.
    drawer : dash_charlotte.Drawer, optional
        The dashboard sidenav.
    id : str, default='dashboard'
        Dashboard ID.

    """

    def __init__(
        self,
        children: Optional[Component] = None,
        id: str = "farm-report",
        className: str = "farm-css",
    ):
        if not isinstance(children, list):
            children = [children]

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
                        dmc.Anchor(
                            "Milk last session",
                            href="/none",
                        ),
                    ]
                ),
                span=5,
                style={
                    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                    "textAlign": "center",
                },
            ),
            dmc.Col(
                html.Div(
                    [
                        dmc.Stack(
                            [
                                dmc.TextInput(
                                    style={"width": 50},
                                    placeholder="235",
                                    disabled=True,
                                ),
                            ],
                            align="flex-end",
                            justify="stretch",
                        )
                    ]
                ),
                span=3,
                offset=3,
                style={
                    "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                    "textAlign": "center",
                },
            ),
        ],
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
                            dmc.Grid(
                                children=[
                                    dmc.Col(
                                        html.Div(
                                            [
                                                dmc.Anchor(
                                                    "Milk last session",
                                                    href="/none",
                                                ),
                                            ]
                                        ),
                                        span=5,
                                        style={
                                            "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                                            "textAlign": "center",
                                        },
                                    ),
                                    dmc.Col(
                                        html.Div(
                                            [
                                                dmc.Stack(
                                                    [
                                                        dmc.TextInput(
                                                            style={"width": 50},
                                                            placeholder="235",
                                                            disabled=True,
                                                        ),
                                                    ],
                                                    align="flex-end",
                                                    justify="stretch",
                                                )
                                            ]
                                        ),
                                        span=3,
                                        offset=3,
                                        style={
                                            "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
                                            "textAlign": "center",
                                        },
                                    ),
                                ],
                                # gutter="xl",
                            ),
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
