#https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from dash import Input, Output, State, callback, dash_table, dcc, html, register_page
from dash.exceptions import PreventUpdate

from componentcallbacks import FertilityReport

register_page(
    __name__,
    path = '/none',
    title = 'Non report'
)




content = dmc.Title('I am here')

layout = FertilityReport(
    children = content,
    id = 'fertility-report-test',
    className = 'fertility-css-test'
)


@callback(Output("fertility-report-test", "data"), Input("global-data", "data"))
def fereport(data):
    df = pd.DataFrame.from_dict(data)

    df = df.loc[:, "index":"group"]


    return df.to_dict("records")
