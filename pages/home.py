import dash
import pandas as pd
from dash import dcc, Input, Output, State, callback, clientside_callback, html
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash_extensions as de
from helpers.choropleth import create_choropleth_chart

CHOROPLETH_INTERVAL = 50

url = 'https://lottie.host/a41f11dd-8351-4a1b-b3ef-540310b13fbf/uS8JUVs5UD.json'
options = dict(loop=True, autoplay=True)

dash.register_page(
    __name__,
    path='/',
    image='home.png',
    title='Space Exploration | Home',
    description='Explore the world of space exploration through a 3D rotating globe, showcasing '
                'the number of launches by country since the dawn of the space age'
)

layout = dmc.Grid(
    [
        dmc.Col(
            [
                dmc.Space(className='main-space', h=20),
                de.Lottie(className='lottie', style={'margin' : '0 auto', 'text-align' : 'center'}, width="81%", height="81%",url=url, options=options, isClickToPauseDisabled=True),
                dmc.Stack(
                    style={'margin-top' : 'auto'},
                    children=[
                        dmc.Title('Атомная история человечества', style={'color': 'white'}, align='center'),
                        dmc.Center(
                            [
                                dmc.Text(
                                    children=[
                                        "Dive into the fascinating world of space missions, launches, and historical "
                                        "milestones. Explore real-time data visualizations and get insights into the "
                                        "future of space exploration."
                                    ],
                                    style={'color': 'white', 'width': '50%'},
                                    align='center',
                                    id='main-text'
                                ),
                            ]
                        ),
                        dcc.Link(
                            [
                                dmc.Button(
                                    'Начать',
                                    id='start-btn',
                                    variant='outline',
                                    color='white',
                                    size='lg',
                                    uppercase=True,
                                    rightIcon=DashIconify(icon='iconoir:radiation', width=30)
                                ),
                            ],
                            href='/historical'
                        )
                    ],
                    align='center',
                    className='stack-left-container',
                    spacing=30,
                    mt=-170
                )
            ],
            md=12, lg=8
        ),
        dmc.Col(
            [
                dmc.Center(
                    className='right-container',
                    id='right-container',
                    children=[
                        dmc.Loader(
                            color="white",
                            size="md",
                            variant="oval"
                        ),
                    ]
                ),
            ], md=12, lg=4
        ),
    ],
    id='home-grid',
    className='hide',
)

@callback(
    Output('right-container', 'children'),
    Input('past-launches-data', 'data'),
)

def create_total_launches_fig(past_launches_data):
    df_launches_per_country = pd.DataFrame(past_launches_data)
    df_launches_per_country = df_launches_per_country[df_launches_per_country['Year'] == 2022]

    return [
        dcc.Graph(
            id='choropleth-fig',
            className='graph-container',
            figure=create_choropleth_chart(df_launches_per_country),
            responsive=True,
            config={
                'displayModeBar': False,
                'scrollZoom': False,
                'doubleClick': False
            }
        ),
        dcc.Interval(id='choropleth-interval', interval=CHOROPLETH_INTERVAL)
    ]


clientside_callback(
    """
    function(className) {
        return "fade-in";
    }
    """,
    Output('home-grid', 'className'),
    Input('home-grid', 'className'),
)

clientside_callback(
    """
    function(_, figure) {
        let rotation_lon = figure.layout.geo.projection.rotation.lon;
        let rotation_lat = figure.layout.geo.projection.rotation.lat;

        if (rotation_lon <= -180) {
            rotation_lon = 180;
        }

        if (rotation_lon >= 180) {
            rotation_lon = -180;
        }

        if (rotation_lat >= 90) {
            rotation_lat = 90;
        } else if (rotation_lat <= -90) {
            rotation_lat = -90;
        }

        if (Math.abs(0 - rotation_lat) < 0.01) {
            rotation_lat = 0;
        }

        const updatedFigure = Object.assign({}, figure);
        updatedFigure.layout.geo.projection.rotation.lon = rotation_lon + 0.5;
        updatedFigure.layout.geo.projection.rotation.lat = rotation_lat;

        return updatedFigure;
    }
    """,
    Output('choropleth-fig', 'figure'),
    Input('choropleth-interval', 'n_intervals'),
    State('choropleth-fig', 'figure'),
    prevent_initial_call=True
)