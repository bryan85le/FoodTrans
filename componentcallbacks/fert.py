from typing import Optional

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, callback, dash_table, dcc, html
from dash.development.base_component import Component
from dash_bootstrap_components import Container


class FertilityReport(Container):
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
        id: str = "fertility-report",
        className: str = "fertility-css",
    ):
        if not isinstance(children, list):
            children = [children]

        super().__init__(
            id=id,
            fluid=True,
            children=self.ferttable(),
            className=className,
        )

    # Create layout for Fertilityy Report
    def ferttable(self) -> dbc.Card:
        return [
            dbc.Card(
                [
                    dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                    dbc.CardBody(
                        [
                            html.H4("Fertility Overview", className="card-title"),
                            html.P(
                                "Some quick example text to build on the card title and make up the bulk of the card's content.",
                                className="card-text",
                            ),
                            dash_table.DataTable(
                                id="tbl-fertility-report",
                            ),
                            html.Br(),
                            dbc.Button("Update", color="primary"),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dcc.Dropdown(
                                ["General Information", "Yeild Milk"],
                                id="loading-states-table-prop",
                            ),
                        ]
                    )
                ]
            ),
        ]

    @callback(Output("tbl-fertility-report", "data"), Input("global-data", "data"))
    def fereport(data):
        df = pd.DataFrame.from_dict(data)
        df = df.loc[:, "index":"group"]

        return df.to_dict("records")
