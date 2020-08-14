import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import pyTigerGraph as tg

import landing_page as lp
import other_page as op


'''
CHOOSE BOOTSTRAP THEME:
----------------------------------------------
    BOOTSTRAP = 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bo...
    CERULEAN = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cerule...
    COSMO = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cosmo/boo...
    CYBORG = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cyborg/b...
    DARKLY = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/darkly/b...
    FLATLY = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/flatly/b...
    GRID = 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstr...
    JOURNAL = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/journal...
    LITERA = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/litera/b...
    LUMEN = 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/lumen/boo...
'''
external_stylesheets = [dbc.themes.DARKLY]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets, 
                suppress_callback_exceptions=True)

'''
app.layout: This method currently set up for multi-page layout.
----------------------------------------------
    dcc.Location:   Used for page navigation.
    dcc.Store:      Used for storing data in the cache / browser
    html.Div:       The main body container where the pages will be loaded into.
'''
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='session', storage_type='session'),
    html.Div(id='page-content'),
])

landing_page = lp.get_page()
other_page = op.get_page()

'''
TigerGraph Connection Parameters:
'''

hostname = "dashtemplate.i.tgcloud.io"
username = "tigergraph"
graphname = "MyGraph"
password = "tigergraph"

conn = tg.TigerGraphConnection(host=hostname,
                                  graphname=graphname,
                                  username=username,
                                  password=password, 
                                  useCert=True)

secret = conn.createSecret()
token = conn.getToken(secret, setToken=True)

print(conn.gsql('ls'))

'''
display_page callback: 
----------------------------------------------
    Output:
        - page-content:  Corresponding page to be displayed from url.    
        - session:       Any data that needs to be stored in browser before loading.

    Input
        - url (pathname):   Url that corresponds to page to be displayed.
        - url (search):     Query string in url if specific id/data to be passed through.

'''
@app.callback([Output('page-content', 'children'),
               Output('session', 'data')],
              [Input('url', 'pathname'),
              Input('url', 'search')])

def display_page(pathname, search):

        data = "some data instead of string if needed."

        if pathname == '/other':
            return [other_page, data]
        
        return [landing_page, data]
        




if __name__=='__main__':
    app.run_server(debug=True)