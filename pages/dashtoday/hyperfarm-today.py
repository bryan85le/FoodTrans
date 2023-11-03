from dash import register_page
from dash_bootstrap_components import Container

from dash import Input, Output, dcc, html, callback

from componentcallbacks.hyperfarm import (
                                            gen_milkpro as gm,
                                            gen_animals_inventory as ga,
                                            gen_health as gh,
                                            gen_fertility as gfe,
                                            gen_groups as gg,
                                            gen_todotoday as gt,
                                            gen_faults as gfa
                                            )



register_page(
    __name__,
    path = '/hyperfarm',
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
