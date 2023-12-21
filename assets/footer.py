import dash_mantine_components as dmc
from dash_iconify import DashIconify

GITHUB_LISA = 'https://github.com/elizaveta-rybina/AtomVisual'
CONTACT_ICON_WIDTH = 25

footer = dmc.Grid(
    [
        dmc.Col(
            [
                dmc.Footer(
                    height=30,
                    fixed=True,
                    className='footer-container',
                    style={
                        'backgroundColor': 'rgba(0,0,0,0)',
                    },
                    mb=5,
                    withBorder=False,
                    children=[
                        dmc.Group(
                            children=[
                                dmc.Anchor(
                                    children=[DashIconify(
                                        icon='mdi:github', width=CONTACT_ICON_WIDTH, className='github-name')
                                    ],
                                    href=GITHUB_LISA
                                )
                            ], position='center'
                        )
                    ]
                )
            ], span=12
        )
    ]
)