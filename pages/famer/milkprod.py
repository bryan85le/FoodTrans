
from dash import dcc, html, Input, Output, callback
import dash_mantine_components as dmc

row1 = html.Tr([html.Td("Milk last session"), html.Td("1284")])
row2 = html.Tr([html.Td("Milk previous day"), html.Td("2764")])
row3 = html.Tr([html.Td("Cows milked last session"), html.Td("67")])
row4 = html.Tr([html.Td("Last 24H average milk per cow"), html.Td("40.1")])
row5 = html.Tr([html.Td("Fat % last 24H"), html.Td("3.65%")])
row6 = html.Tr([html.Td("Protein % last 24H"), html.Td("3.28")])


layout = html.Div([
    html.H3('Milk productions'),
    dmc.Table(
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
        ),
    dcc.Dropdown(
        {f'Page 1 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
        id='page-1-dropdown'
    ),
    html.Div(id='page-1-display-value'),
])


@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'