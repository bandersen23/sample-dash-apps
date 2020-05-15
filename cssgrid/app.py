#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:26:31 2020

@author: brandonandersen
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import flask

server = flask.Flask(__name__)
app = dash.Dash(server=server)

# run with the following:
# gunicorn app:server -b :8000

app.layout = html.Div(className='wrapper',
                      children=[
                              html.Div(className='header', children=dcc.Markdown('Page Title')),
                              html.Div(className='menu', children=dcc.Markdown('Menu')),
                              html.Div(className='top-content', children=dcc.Markdown('Top Content')),
                              html.Div(className='bottom-content', children=dcc.Markdown('Bottom Content'))
                              ])

if __name__ == '__main__':
    app.run_server()
