# confirmation.py
from dash import Dash, html

app = Dash(__name__, external_stylesheets=['assets/styles_cf.css'])

# Nội dung trang xác nhận
def create_confirmation_page(data):
    if data:
        return html.Div(
            children=[
                html.H1("Fora Users Log"),
                html.H2("Manage access requests for Fora"),
                html.P(f"First Name: {data.get('first_name', '')}"),
                html.P(f"Last Name: {data.get('last_name', '')}"),
                html.P(f"Email Address: {data.get('email', '')}"),
                html.P(f"Title: {data.get('title', '')}"),
                html.P(f"Function: {data.get('function', '')}")
            ]
        )
    return html.Div(
        children=[
            html.H1("Fora Users Log"),
            html.P("No data available.")
        ]
    )

