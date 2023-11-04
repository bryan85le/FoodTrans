# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dash_table, dcc, html, register_page
from dash.exceptions import PreventUpdate

from componentcallbacks import Farmtoday

register_page(__name__, path="/farmtoday", title="Farmer Today report res")


content = dmc.Title("I am here")

layout = Farmtoday(
    children=content,
    id="farm-report-test",
)


@callback(Output("farm-report-test", "data"), Input("global-data", "data"))
def fereport(data):
    df = pd.DataFrame.from_dict(data)
    df = df.loc[:, "index":"group"]

    return df.to_dict("records")
