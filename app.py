import dash
from dash import Dash, html, dcc, Output, Input, callback
from dash_bootstrap_components.themes import BOOTSTRAP
from assets.footer import footer

def main() -> None:
    app = Dash(
        __name__,
        external_stylesheets=[BOOTSTRAP],
        use_pages=True
        )
    app.layout = html.Div(
    [
        dash.page_container,
        footer
    ]
)
    app.run()

if __name__ == "__main__":
    main()