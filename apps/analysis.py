import dash_core_components as dcc
from dash import html
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app

# needed only if running this as a single page app
# external_stylesheets = [dbc.themes.LUX]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# change to app.layout if running as single page app instead
# the style arguments for the sidebar. We use position:fixed and a fixed width
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#figure6
df_m= pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/Movies.csv")
list_count_by_Movie_Genre=df_m['Movie_Genre'].value_counts()
list_count_by_Movie_Genre_list=list(list_count_by_Movie_Genre.index)
fig6= px.bar(df_m, x=list_count_by_Movie_Genre.index ,y=list_count_by_Movie_Genre)

total_count=len(df_m)
df_g = df_m.groupby(['Movie_Genre']).size().reset_index()

df_g['percentage'] = df_m.groupby(['Movie_Genre']).size().groupby(level=0).apply(lambda x: 100 * x / total_count).values
df_g.columns = ['Movie_Genre', 'Counts', 'Percentage']
df_g=df_g.sort_values(by=['Counts'],ascending=False)
fig6=px.bar(df_g, x='Movie_Genre', y=['Counts'], text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
fig6.update_traces(marker_color='green')

#figure7
df_s= pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/Series.csv")
list_count_by_Series_Genre=df_s['Series_Genre'].value_counts()
list_count_by_Series_Genre_list=list(list_count_by_Series_Genre.index)
fig7= px.bar(df_s, x=list_count_by_Series_Genre.index ,y=list_count_by_Series_Genre)

total_count1=len(df_s)
df_g = df_s.groupby(['Series_Genre']).size().reset_index()

df_g['percentage'] = df_s.groupby(['Series_Genre']).size().groupby(level=0).apply(lambda x: 100 * x / total_count).values
df_g.columns = ['Series_Genre', 'Counts', 'Percentage']
df_g=df_g.sort_values(by=['Counts'],ascending=False)
fig7=px.bar(df_g, x='Series_Genre', y=['Counts'], text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
fig7.update_traces(marker_color='orange')

#figure8
df_l= pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/Languages preferred.csv")
list_count_by_Languages_Preferred=df_l['Languages_Preferred'].value_counts()
list_count_by_Languages_Preferred_list=list(list_count_by_Languages_Preferred.index)
fig8= px.bar(df_l, x=list_count_by_Languages_Preferred.index ,y=list_count_by_Languages_Preferred)

total_count=len(df_l)
df_g1 = df_l.groupby(['Languages_Preferred']).size().reset_index()

df_g1['percentage'] = df_l.groupby(['Languages_Preferred']).size().groupby(level=0).apply(lambda x: 100 * x / total_count).values
df_g1.columns = ['Languages_Preferred', 'Counts', 'Percentage']
df_g1=df_g1.sort_values(by=['Counts'],ascending=False)
fig8=px.bar(df_g1, x='Languages_Preferred', y=['Counts'], text=df_g1['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))
fig8.update_traces(marker_color='brown')

#figure9
df_n = pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/fornem.csv")
fig9 = px.scatter(df_n, x="OTT_Platforms" ,
                 y="Age_Category", animation_frame="Occupational_Status",
                 color="Gender",range_y=[0,100],size_max=25, size='Age_Category')



layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("MOVIES AND SERIES ANALYSIS"), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising trends across the different parts of India'), className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Genre Preferences',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(children='Genre Preferences in Movies', className="text-center"),
                    width=6, className="mt-4"),
            dbc.Col(html.H5(children='Genre Preferences in Series', className="text-center"), width=6, className="mt-4"),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='mgenre',figure=fig6), width=6),
            dbc.Col(dcc.Graph(id='sgenre',figure=fig7), width=6)
        ]),
dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Most Preferred Languages',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mt-4 mb-5")
        ]),

dbc.Row([
            dbc.Col(html.H5(children='Percentage Distribution', className="text-center"),
                    className="mt-4"),
        ]),

        dcc.Graph(id='languages',figure=fig8),

    ]),

dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='OTT Platforms preferred among various Age Category',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mt-4 mb-5")
        ]),

dbc.Row([
            dbc.Col(html.H5(children='Trend in the usage of OTT Platforms among various Age Category vs Occupational Status', className="text-center"),
                    className="mt-4"),
        ]),

        dcc.Graph(id='ott',figure=fig9),

    ])

