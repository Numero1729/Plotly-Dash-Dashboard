from dash import html
import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
# change to app.layout if running as single page app instead
from app import app

layout = html.Div([
    html.Img(src=app.get_asset_url('final.jpeg'), style={'height':'100%', 'width':'100%'})
],
)

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)