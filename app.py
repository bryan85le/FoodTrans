# Native Python packages
import logging
from socket import gethostname

# Web stuff
from dash import (
    Dash,
    Input,
    Output,
    State,
    callback,
    dcc,
    html,
    no_update,
    page_container,
)
from flask import Flask

# Charlotte components
from components import (
    Dashboard,
    Drawer,
    DrawerFooter,
    DrawerMultiItem,
    DrawerSingleItem,
    DrawerSubItem,
    Navbar,
)
from pages.login.login_auth import LoginAuth

# Create server with secret key
server = Flask(__name__)
server.secret_key = 'SECRET_KEY'



# Instanciate Dash app
app = Dash(
    name = __name__,
    server = server,
    title = 'NZ Hyper',
    use_pages = True,
    update_title = 'Updating...',
)



# Instanciate Error Handler
file_handler = logging.FileHandler('data/errorlog.log')
file_handler.setLevel(logging.WARNING)
server.logger.addHandler(file_handler)



# Create Drawer
nav_links = [
    DrawerSingleItem(
        name = 'Login',
        icon = 'bx:log-in',
        href = '/login'
    ),
    DrawerSingleItem(
        name = 'Page 1',
        icon = 'bx:scatter-chart',
        href = '/page1'
    ),
    DrawerMultiItem(
        name = 'Page2',
        icon = 'bx:line-chart',
        href = '/page2/subpage1',
        submenu = [
            DrawerSubItem(
                name = 'Subpage 1',
                href = '/page2/subpage1'
            ),
            DrawerSubItem(
                name = 'Subpage 2',
                href = '/page2/subpage2'
            )
        ]
    ),
    DrawerFooter(
        title = 'Footer',
        subtitle = 'Footer Subtitle'
    )
]


# Create a global data excell
import pandas as pd

df = pd.read_csv('data/hyperFarm.csv')

InitData = html.Div(
    [
        dcc.Store(id='global-data'),
        html.Div(id="dump-inputdata")
    ]
)

@callback(Output('global-data', 'data'),
          Input('dump-inputdata', 'children'),
          State('global-data', 'data'),
        prevent_initial_call=False
        )
def filter_countries(_, data):
    if data is None:
        #raise PreventUpdate
        return df.to_dict('records')
    return data


# Create Dashboard Layout
app.layout = Dashboard(
    children = page_container,
    id = 'dashboard',
    navbar = Navbar(
        title = 'My Web App',
        id = 'dashboard-navbar'
    ),
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        logo_icon = 'heroicons:rocket-launch-20-solid'
    ),
    initialdata = InitData,

)



# Run app
if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000
    )
