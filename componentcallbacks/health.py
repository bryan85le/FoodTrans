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

from .functions import tlbContent


class Health(Container):
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
                    dbc.CardImg(src="/assets/img/register.svg", top=True),
                    dbc.CardBody(
                        [
                            html.H3("Milk Production"),
                            tlbContent(title="Milk last session"),
                            tlbContent(title="Milk previous day"),
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
                        ]
                    ),
                ],
                # style={"width": "20rem"},
            ),
        ]
