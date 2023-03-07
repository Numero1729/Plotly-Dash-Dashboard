import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
from dash import html
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#figure10
df_time= pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/Time Spent.csv")
list_count_by_Time_Spent=df_time['Time_Spent'].value_counts()
list_count_by_Time_Spent_list=list(list_count_by_Time_Spent.index)
fig10= px.bar(df_time,x=list_count_by_Time_Spent.index ,y=list_count_by_Time_Spent)

total_count=len(df_time)
df_g2 = df_time.groupby(['Time_Spent']).size().reset_index()

df_g2['percentage'] = df_time.groupby(['Time_Spent']).size().groupby(level=0).apply(lambda x: 100 * x / total_count).values
df_g2.columns = ['Time_Spent', 'Counts', 'Percentage']
df_g2=df_g2.sort_values(by=['Counts'],ascending=False)
fig10=px.bar(df_g2, x='Time_Spent', y=['Counts'], text=df_g2['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))

#figure11
df_d= pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/devices.csv")
list_count_by_Device_Used=df_d['Device_Used'].value_counts()
list_count_by_Device_Used_list=list(list_count_by_Device_Used.index)
fig11= px.bar(df_d, x=list_count_by_Device_Used.index ,y=list_count_by_Device_Used)

total_count7=len(df_d)
df_g3 = df_d.groupby(['Device_Used']).size().reset_index()

df_g3['percentage'] = df_d.groupby(['Device_Used']).size().groupby(level=0).apply(lambda x: 100 * x / total_count).values
df_g3.columns = ['Device_Used', 'Counts', 'Percentage']
df_g3=df_g3.sort_values(by=['Counts'],ascending=False)
fig11 = px.pie(values=list_count_by_Device_Used, names=list_count_by_Device_Used.index)


layout = html.Div([
    dbc.Container([
dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Time Spent on OTT Platforms',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(children=[], className="text-center"),
                    className="mt-4"),
        ]),

        dcc.Graph(id='time',figure=fig10),

dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Devices Used',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(children=[], className="text-center"),
                    className="mt-4"),
        ]),

        dcc.Graph(id='devices',figure=fig11),

        ])
    ])