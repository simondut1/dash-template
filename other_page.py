import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import navbar as nb

import navbar as nb

navbar = nb.get_navbar()
text = html.P('other page')

other_page = html.Div([navbar, text])

def get_page():
    return other_page