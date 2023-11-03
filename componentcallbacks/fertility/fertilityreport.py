# https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import Input, Output, State, callback, dash_table, dcc, html, register_page

from componentcallbacks.fertility import graphreport as gr
from componentcallbacks.fertility import inseminationwindow as ins

layout = dmc.Container(
    [
        dbc.Collapse(
            ins.layout,
            id="collapse2",
            is_open=True,
        ),
        dbc.Collapse(
            gr.layout,
            id="collapse1",
            is_open=True,
        ),
    ],
    fluid=True,
)


@callback(
    Output("collapse1", "is_open"),
    Output("collapse2", "is_open"),
    [Input("tbl", "active_cell")],
    [State("collapse1", "is_open")],
    [State("collapse2", "is_open")],
)
def toggle_collapse(active_cell, is_open1, is_open2):
    if active_cell["column_id"] == "Cow Yeild":
        return 1, 1
    elif active_cell["column_id"] == "Cow Sign":
        return 0, 1
    elif active_cell["column_id"] == "Status":
        return 1, 0
    return 0, 0
