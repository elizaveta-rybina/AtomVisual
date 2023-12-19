import dash
import pandas as pd
from dash import html, dcc, Output, Input, callback
from assets.footer import footer
from pages.nav import navbar
from helpers.cloud_storage import read_from_gcs
from io import StringIO

app = dash.Dash(
    __name__,
    title='Space Exploration',
    use_pages=True,
    update_title=False,
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True
)

app.layout = html.Div(
    [
        navbar(),
        dash.page_container,
        footer,
        dcc.Store(id='past-launches-data'),
    ]
)

@callback(
    Output('past-launches-data', 'data'),
    Input('past-launches-data', 'id'),
)

def load_past_launches_data(_):
    df = pd.read_csv('data/nuclear-warhead-stockpiles.csv')
    dff = df.to_dict('records')
    return dff
    # df = pd.read_csv('data/nuclear-warhead-stockpiles.csv')
    # dff = df[df['Year'] == '2022']
    # dff_data = dff.to_dict('records')
    # return dff_data

if __name__ == "__main__":
    app.run_server(debug=False)