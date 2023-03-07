import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
from dash import html
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

layout = html.Div([
dbc.Container([
dbc.Row([
html.Img(src=app.get_asset_url('one.jpg'), style={'height':'100%', 'width':'100%'}),
html.Img(src=app.get_asset_url('two.jpg'), style={'height':'100%', 'width':'100%'}),
html.Img(src=app.get_asset_url('three.jpg'), style={'height':'100%', 'width':'100%'}),
html.Img(src=app.get_asset_url('four.jpg'), style={'height':'100%', 'width':'100%'}),
html.Img(src=app.get_asset_url('five.jpg'), style={'height':'100%', 'width':'100%'}),
    ])
    ])
])
