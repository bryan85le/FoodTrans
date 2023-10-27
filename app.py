# Native Python packages
import logging
from socket import gethostname

# Web stuff
from dash import (
    Dash,
    Input,
    Output,
    no_update,
    page_container
)
from flask import Flask

# Charlotte components
from components import (
    Dashboard,
    Drawer,
    DrawerSingleItem,
    DrawerMultiItem,
    DrawerSubItem,
    DrawerFooter,
    Navbar
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
    )
)



# Run app
if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000
    )
