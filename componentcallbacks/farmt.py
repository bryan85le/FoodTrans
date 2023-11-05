import datetime
import random
import uuid
from typing import Optional

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import MATCH, Input, Output, State, callback, dash_table, dcc, html
from dash.development.base_component import Component
from dash_bootstrap_components import Container

from .functions import tlbContent


class FarmToday(Container):
    """Container report.

    Parameters
    ----------
    id : str, default='health-report'
        Dashboard ID.
    """

    df = px.data.tips()
    fig = px.pie(df, values="tip", names="day")

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
                    dbc.CardImg(src="/assets/img/register.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Milk Production"),
                            tlbContent(title="Milk last session"),
                            tlbContent(title="Milk previous day"),
                            tlbContent(title="Cows milked last session"),
                            tlbContent(title="Last 24H average milk per cow"),
                            tlbContent(title="Fat % last 24H"),
                            tlbContent(title="Protein % last 24H"),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/register.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Health"),
                            tlbContent(title="Mastitis"),
                            tlbContent(title="Degestion Problems"),
                            tlbContent(title="Ketosis"),
                            tlbContent(title="Fresh cows to check"),
                            tlbContent(title="Non-specific health report"),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/register.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Groups"),
                            tlbContent(title="Welfare alerts(in groups)"),
                            tlbContent(title="Nutrition alerts"),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/register.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Todo to today"),
                            tlbContent(title="To dry today"),
                            tlbContent(title="Due calving"),
                            tlbContent(title="Sorted Animals"),
                            tlbContent(title="For pregnacny check"),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/register.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Faults today"),
                            tlbContent(title="Un-Assigned Tags"),
                            tlbContent(title="Not Identified in Milking"),
                            tlbContent(title="In Milking"),
                            tlbContent(title="Wrong Group"),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardImg(src="/assets/img/register.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Animals Invetory"),
                            tlbContent(title="Cows"),
                            tlbContent(title="Pregnant Milk"),
                            tlbContent(title="Open"),
                            tlbContent(title="Dry"),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            dcc.Graph(figure=self.fig),
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
        ]
