import dash
from dash import dcc, callback, Input, Output, clientside_callback
import dash_mantine_components as dmc
from helpers.map import create_map
from helpers.histogram import create_histogram_station
import numpy as np
import pandas as pd

dash.register_page(
    __name__,
    image='historical.png',
    title='Space Exploration | Atom',
    description='Dive into the key milestones of space exploration, presented in a unique cytoscape constellation '
                'format. Each point represents a significant event, complete with descriptions and images'
)

nuclear_plants=pd.read_csv("./data/nuclear_power_plants.csv",delimiter=';',encoding='latin1')
nuclear_plants = nuclear_plants.drop(0)
nuclear_plants = nuclear_plants.reset_index(drop=True)
nuclear_plants.dropna(subset=['Latitude', 'Longitude', 'Capacity'], inplace=True)
columns_to_fill = nuclear_plants.columns.difference(['OperationalTo'])
nuclear_plants[columns_to_fill] = nuclear_plants[columns_to_fill].fillna('Unknown')
nuclear_plants['OperationalTo'] = np.where(nuclear_plants['OperationalFrom'] == 'Unknown', 'Unknown', nuclear_plants['OperationalTo'])
nuclear_plants['OperationalTo'] = np.where((nuclear_plants['OperationalTo'].isnull()) & (nuclear_plants['OperationalFrom'] != 'Unknown'), 'Ongoing', nuclear_plants['OperationalTo'])

layout = dmc.Grid(
    [
        dmc.Title('Мирный атом',className="main-title-map", style={'textAlign': 'center'}, color='white', align='center'),
        dmc.Col(
            className='atom-container',
            children=[
                dcc.RadioItems(
                    id='visualization-type',
                    className='visualization-type',
                    options=[
                        {'label': 'Карта ядерных электростанций', 'value': 'map'},
                        {'label': 'Гистограмма атомных станций по годам', 'value': 'histogram'},
                    ],
                    value='map',  # значение по умолчанию
                    labelStyle={'display': 'inline'},
                    inputStyle={"border-radius": "10px"}
                ),
                dcc.Graph(
                    id='visualization-output',
                    className='visualization-output'
                ),
            ],
        ),
    ],
    id='map-grid',
    className='map'
)

@callback(
    Output('visualization-output', 'figure'),
    [Input('visualization-type', 'value')]
)

def update_visualization(selected_type):
    if selected_type == 'map':
        return create_map(nuclear_plants)
    elif selected_type == 'histogram':
        return create_histogram_station(nuclear_plants)
        

clientside_callback(
    """
    function(className) {
        return "fade-in";
    }
    """,
    Output('map-grid', 'className'),
    Input('map-grid', 'className'),
)