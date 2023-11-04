from dash import Input, Output, callback, dcc, html, register_page
from dash_bootstrap_components import Container

from componentcallbacks.hyperfarm import gen_animals_inventory as ga
from componentcallbacks.hyperfarm import gen_faults as gfa
from componentcallbacks.hyperfarm import gen_fertility as gfe
from componentcallbacks.hyperfarm import gen_groups as gg
from componentcallbacks.hyperfarm import gen_health as gh
from componentcallbacks.hyperfarm import gen_milkpro as gm
from componentcallbacks.hyperfarm import gen_todotoday as gt

register_page(
    __name__,
    path = '/hyperdash',
    title = 'Dash'
)



layout = html.Div(
    [
        gm.layout,
        ga.layout,
        gh.layout,
        gfe.layout,
        gg.layout,
        gt.layout,
        gfa.layout

    ]
)
