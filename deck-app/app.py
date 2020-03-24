#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:08:33 2020

@author: brandonandersen
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import jinja2
import yaml

with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

MAPBOX_KEY = config['MAPBOX_API_KEY']
templateLoader = jinja2.FileSystemLoader(searchpath="templates")
templateEnv = jinja2.Environment(loader=templateLoader)

app = dash.Dash()
app.layout = html.Div([
    dcc.Markdown(children=['This is a demo of pydeck and dash.  ', 
                           'We are using the hexagon example from here: ',
                           'https://deckgl.readthedocs.io/en/stable/layer.html#pydeck.bindings.layer.Layer  '
                           ]),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Dark', 'value': 'dark'},
            {'label': 'Light', 'value': 'light'}
        ],
        value='dark'
    ),
    html.Div(id='target', style={"height":"80vh"})
])


@app.callback(Output('target', 'children'), [Input('dropdown', 'value')])
def embed_iframe(value):
    template = templateEnv.get_template(f'hexagon-example-{value}.html')
    src = template.render(MAPBOX_API_KEY=MAPBOX_KEY)
        
    return html.Iframe(srcDoc=src, height="100%", width="100%")


if __name__ == '__main__':
    app.run_server()