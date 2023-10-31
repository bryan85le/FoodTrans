#https://www.afimilk.com/docs/documents/afifarm/anestrus%20report.htm?tocpath=_____5
from dash import Input, Output, dcc, html, callback, register_page, dash_table
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np
data = px.data.gapminder()


layout = dmc.Container(
    [
        html.H4('Life expentancy progression of countries per continents'),
        dash_table.DataTable(
                    data.to_dict("records"),
                    [{"name": i, "id": i} for i in data.columns],
                    id='tbl',
                    page_size=10,
                    style_table={"overflow-x": "auto"},
                ),
        dcc.Graph(id="graph"),
        dcc.Checklist(
            id="checklist",
            options=["Asia", "Europe", "Africa","Americas","Oceania"],
            value=[],
            inline=True
        ),
        dbc.Alert(id='tbl_out'),

    ],
    fluid=True,
)



@callback(
    Output("graph", "figure"),
    Output('tbl_out', 'children'),
    Input('tbl', 'active_cell')
    )
def update_line_chart(active_cell):
    df = px.data.gapminder() # replace with your own data source
    rw = active_cell['row']
    cownum = np.array([df.at[rw,'continent']])

    mask = df.continent.isin(cownum)
    fig = px.line(df[mask], 
        x="year", y="lifeExp", color='country')
    return fig, str(active_cell)




