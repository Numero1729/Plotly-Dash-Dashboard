import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
from dash import html
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

# needed if running single page dash app instead
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#plotting our graphs
import pandas as pd
import plotly.express as px
import json
from urllib.request import urlopen
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd
import plotly

#figure 1
df = pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/OTT Platforms.csv")
list_count_by_Gender=df['Gender'].value_counts()
list_count_by_Gender_list=list(list_count_by_Gender.index)
fig1 = px.pie(values=list_count_by_Gender, names=list_count_by_Gender.index)

#figure2
df1 = pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/Series.csv")
list_count_by_Residence=df['Residence'].value_counts()
list_count_by_Residence_list=list(list_count_by_Residence.index)
fig2 = px.pie(values=list_count_by_Residence, names=list_count_by_Residence.index ,title="Residence")

#figure3
list_count_by_Occupational_Status = df1['Occupational_Status'].value_counts()
list_count_by_Occupational_Status_list = list(list_count_by_Occupational_Status.index)
fig3 = px.bar(df1, x=list_count_by_Occupational_Status.index ,y=list_count_by_Occupational_Status)
total_count=len(df1)
df_g = df1.groupby(['Occupational_Status']).size().reset_index()
df_g['percentage'] = df1.groupby(['Occupational_Status']).size().groupby(level=0).apply(lambda x: 100 * x / total_count).values
df_g.columns = ['Occupational_Status', 'Counts', 'Percentage']
df_g=df_g.sort_values(by=['Counts'],ascending=False)
fig3=px.bar(df_g, x='Occupational_Status', y=['Counts'], text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))

#figure4
list_count_by_age=df['Age_Category'].value_counts()
list_count_by_age_list=list(list_count_by_age.index)
fig4= px.bar(df, x=list_count_by_age.index ,y=list_count_by_age)
total_count1=len(df)
df_g = df.groupby(['Age_Category']).size().reset_index()
df_g['percentage'] = df.groupby(['Age_Category']).size().groupby(level=0).apply(lambda x: 100 * x / total_count).values
df_g.columns = ['Age_Category', 'OTT_Platforms', 'Percentage']
df_g=df_g.sort_values(by=['OTT_Platforms'],ascending=False)
fig4=px.bar(df_g, x='Age_Category', y=['OTT_Platforms'], text=df_g['Percentage'].apply(lambda x: '{0:1.2f}%'.format(x)))


#figure5
states = pd.read_csv("C:/Users/anton/PycharmProjects/Project-Dashboard/states.csv")
state_count_df=states.groupby(['State']).size().reset_index(name = 'counts')
geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
response = urlopen(geojson)
data_json = json.loads(response.read())
df_json=pd.DataFrame(data_json)
state_array = []
for i in range(len(df_json['features'])):
    state_name=pd.DataFrame(df_json['features'][i]).loc['ST_NM'].properties
    state_array.append(state_name)
df_all_states = pd.DataFrame(state_array,columns = ['State'])
df2 = pd.merge(df_all_states, state_count_df, on='State', how='left')
df2 = df2.fillna(0)
fig5 = px.choropleth(
    df2,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='counts',
    color_continuous_scale='Reds'
)
fig5.update_geos(fitbounds="locations", visible=False)


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='SURVEY ON OTT PLATFORM'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising movies and series trends across India'), className="mb-4")
        ]),
        # for some reason, font colour remains black if using the color option
        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='SUMMARY OF OUR DATA',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mt-4 mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='Gender Distribution', className="text-center"),
                    width=4, className="mt-4"),
            dbc.Col(html.H5(children='Age-Category Distribution', className="text-center"), width=8, className="mt-4"),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='gender',figure=fig1), width=4),
            dbc.Col(dcc.Graph(id='ageCat',figure=fig4), width=8)
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='OUR RESPONDERS LOCATION SUMMARY',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(children='Locations', className="text-center"),
                    width=6, className="mt-4"),
            dbc.Col(html.H5(children='Residence Type', className="text-center"), width=4,
                    className="mt-4"),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='location',figure=fig5), width=6),
            dbc.Col(dcc.Graph(id='residence',figure=fig2), width=4)
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(html.H3(children='Occupational Status',
                                     className="text-center text-light bg-dark"), body=True, color="dark")
                    , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(children='Percentage Distribution', className="text-center"),
                    className="mt-4"),
        ]),

        dcc.Graph(id='occupation',figure=fig3),

    ])

])




# needed only if running this as a single page app
#if __name__ == '__main__':
 #    app.run_server(host='127.0.0.1', debug=True)
