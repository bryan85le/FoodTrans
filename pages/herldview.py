from dash import register_page
from dash_bootstrap_components import Container

from components import Box



register_page(
    __name__,
    path = '/herldview',
    title = 'Herld Vierw'
)



layout = Container(
    children = Box(
        children = 'Content',
        title = 'Page 1'
    ),
    className = 'mt-4'
)
