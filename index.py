import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# must add this line in order for the app to be deployed successfully on Heroku
from app import server
from app import app
# import all pages in the app
from apps import overview, analysis, home, miscell, tests

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dcc.Link("Home", href="/home", className="dropdown-item"),
        dcc.Link("Overview", href="/overview", className="dropdown-item"),
        dcc.Link("Analysis", href="/analysis", className="dropdown-item"),
        dcc.Link("Miscellaneous", href="/miscell", className="dropdown-item"),
        dcc.Link("Tests Done !!", href="/tests", className="dropdown-item"),
    ],
    nav=True,
    in_navbar=True,
    label="Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="C:/Users/anton/PycharmProjects/Project-Dashboard/assets/vadapav.jpeg", height="30px")),
                        dbc.Col(dbc.NavbarBrand("TEAM VADA PAV", className="ml-2")),
                    ],
                    align="center",
                    className="no-gutters"
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
    sticky="top"
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

    # embedding the navigation bar
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        navbar,
        html.Div(id='page-content')
    ])


    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/overview':
            return overview.layout
        elif pathname == '/analysis':
            return analysis.layout
        elif pathname == '/miscell':
            return miscell.layout
        elif pathname == '/tests':
            return tests.layout
        else:
            return home.layout


    if __name__ == '__main__':
        app.run_server(debug=True)