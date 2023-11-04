
# Native Python packages
import logging
from socket import gethostname

import dash

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


# Create Dashboard Layout
app.layout = dash.page_container



# Run app
if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000
    )
