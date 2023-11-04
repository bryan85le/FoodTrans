# Import packages
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
dash.register_page(__name__, path='/farmers/milk-production', external_stylesheets=external_stylesheets)

# App header
header = dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3")



# Content of Tab1

milk_consumption = dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3")




#-------------------------------------------------------------------------------------------------------------------
# App Content1


row1 = html.Tr([html.Td("Milk last session"), html.Td("1284")])
row2 = html.Tr([html.Td("Milk previous day"), html.Td("2764")])
row3 = html.Tr([html.Td("Cows milked last session"), html.Td("67")])
row4 = html.Tr([html.Td("Last 24H average milk per cow"), html.Td("40.1")])
row5 = html.Tr([html.Td("Fat % last 24H"), html.Td("3.65%")])
row6 = html.Tr([html.Td("Protein % last 24H"), html.Td("3.28")])

content = dmc.Table(
    striped=True,
    highlightOnHover=True,
    withBorder=True,
    withColumnBorders=True,
    children=[
        row1,
        row2,
        row3,
        row4,
        row5,
        row6,
        
    ]
)


# Content 1 layout
content1 = dmc.Container([
    dmc.Grid([
        dmc.Col([
            dmc.Title(f"Milk production", order=1),
            content
        ], span=6),
    ]),
], fluid=True)

#------------------------------------------------------------------------------------









# Main content
main_content = html.Div(
    children=[
        content1,

    ]
)



#App main layout

layout = html.Div(
    children=[
        #header,
        #bartitle,
        main_content,
        #footer,
    ]
)