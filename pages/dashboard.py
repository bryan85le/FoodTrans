# Import packages
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
from pages.famer import milkprod

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
dash.register_page(__name__, path='/', external_stylesheets=external_stylesheets)

# App header
header = dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3")



# Content of Tab1

milk_consumption = dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3")




#-------------------------------------------------------------------------------------------------------------------
# App Content1


content = milkprod.layout


# Content 1 layout
content1 = dmc.Container([
    dmc.Grid([
        dmc.Col([
            dmc.Title(f"Milk production", order=1),
            content
        ],       ),
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