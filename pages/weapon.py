import dash
from dash import dcc, callback, Input, Output, clientside_callback
import dash_mantine_components as dmc
from helpers.linear import create_linear
from helpers.histogram import create_histogram_weapon
import numpy as np
import pandas as pd

dash.register_page(
    __name__,
    image='insights.png',
    title='Space Exploration | Weapon',
    description='Get real-time analytics on space launches. Interactive dashboards allow you to filter by year, '
                'providing insights into launch success rates, most active organizations, and more'
)

nuclear_plants=pd.read_csv("./data/nuclear_power_plants.csv",delimiter=';',encoding='latin1')
nuclear_test=pd.read_csv("./data/number-of-nuclear-weapons-tests.csv")
nuclear_number = pd.read_csv("./data/nuclear-warhead-stockpiles.csv")

layout = dmc.Grid(
    [
        dmc.Title('Ядерное оружие',className="main-title-weapon", style={'textAlign': 'center'}, color='white', align='center'),
        dmc.Col(
            className='weapon-container',
            children=[
                dcc.RadioItems(
                    id='visualization-type-weapon',
                    className='visualization-type-weapon',
                    options=[
                        {'label': 'Гистограмма ядерных испытаний', 'value': 'histogram'},
                        {'label': 'Линейный график ядерных запасов', 'value': 'linear'},
                    ],
                    value='histogram',  # значение по умолчанию
                    labelStyle={'display': 'inline'},
                    inputStyle={"border-radius": "10px"}
                ),
                dcc.Graph(
                    id='visualization-output-weapon',
                    className='visualization-output-weapon'
                ),
            ],
        ),
    ],
    id='weapon-grid',
    className='weapon'
)

@callback(
    Output('visualization-output-weapon', 'figure'),
    [Input('visualization-type-weapon', 'value')]
)

def update_visualization(selected_type):
    if selected_type == 'linear':
        return create_linear(nuclear_number)
    elif selected_type == 'histogram':
        return create_histogram_weapon(nuclear_test)
        

clientside_callback(
    """
    function(className) {
        return "fade-in";
    }
    """,
    Output('weapon-grid', 'className'),
    Input('weapon-grid', 'className'),
)

      