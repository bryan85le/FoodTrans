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
        id: str = "farm-report",
        className: str = "farm-css",
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
