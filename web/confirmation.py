import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"])

# Sample data
data = [
    {"email": "...", "first_name": "Ally", "last_name": "Melrod", "role": "Inactive"},
    {"email": "kimberly.howze@orionworldwide.com", "first_name": "Kimberly", "last_name": "Howze", "role": "Inactive"}
]

# Layout
app.layout = dbc.Container(
    [
        html.H1("Fora Users Log", className="mt-5"),
        html.P("Manage access requests for Fora."),
        
        dbc.Tabs(
            [
                dbc.Tab(label="Users", tab_id="users"),
                dbc.Tab(label="Access Requests (2)", tab_id="access_requests", activeTabClassName="fw-bold"),
                dbc.Tab(label="Roles", tab_id="roles"),
            ],
            id="tabs",
            active_tab="access_requests",
            className="mt-3"
        ),
        
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button("Sort", outline=True, color="secondary", className="me-1"),
                    width="auto"
                ),
                dbc.Col(
                    dbc.Button("Filter", outline=True, color="secondary", className="me-1"),
                    width="auto"
                ),
                dbc.Col(width="8"),
                dbc.Col(
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText(html.I(className="fa fa-search")),
                            dbc.Input(placeholder="Search for users by name or email address"),
                        ]
                    ),
                    width="4"
                ),
            ],
            className="align-items-center mt-3"
        ),
        
        dbc.Row(
            [
                dbc.Col(html.H5("2 Access Requests"), width="auto", className="mt-4"),
                dbc.Col(width="7"),
                dbc.Col(
                    dbc.Button("Export User List", outline=True, color="secondary", className="me-2"),
                    width="auto",
                    className="mt-4"
                ),
                dbc.Col(
                    dbc.Button("Delete Selected User", color="dark", className="me-2"),
                    width="auto",
                    className="mt-4"
                ),
                dbc.Col(
                    dbc.Button("Add New User", color="primary"),
                    width="auto",
                    className="mt-4"
                ),
            ],
        ),
        
        dbc.Table(
            [
                html.Thead(
                    html.Tr(
                        [
                            html.Th(dbc.Checkbox(), scope="col"),
                            html.Th("Email Address"),
                            html.Th("First Name"),
                            html.Th("Last Name"),
                            html.Th("User Role"),
                            html.Th("Status"),
                            html.Th("Review"),
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Th(dbc.Checkbox(), scope="row"),
                                html.Td(data[0]["email"]),
                                html.Td(data[0]["first_name"]),
                                html.Td(data[0]["last_name"]),
                                html.Td(data[0]["role"]),
                                html.Td(
                                    dbc.Button("Inactive", color="secondary", size="sm", disabled=True)
                                ),
                                html.Td(dbc.Button("Review", color="link")),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th(dbc.Checkbox(), scope="row"),
                                html.Td(data[1]["email"]),
                                html.Td(data[1]["first_name"]),
                                html.Td(data[1]["last_name"]),
                                html.Td(data[1]["role"]),
                                html.Td(
                                    dbc.Button("Inactive", color="secondary", size="sm", disabled=True)
                                ),
                                html.Td(dbc.Button("Review", color="link")),
                            ]
                        ),
                    ]
                ),
            ],
            bordered=True,
            hover=True,
            responsive=True,
            className="mt-3"
        ),
    ],
    fluid=True,
    className="p-5"
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
