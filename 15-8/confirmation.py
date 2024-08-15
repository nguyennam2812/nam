import dash_bootstrap_components as dbc
from dash import html

# Hàm tạo nội dung trang quản lý người dùng
def create_confirmation_page(data):
    return dbc.Container(
        [
            html.H1("Fora Users Log", className="mt-5"),
            html.P("Manage access requests for Fora."),
            
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button("Users", id="users-tab", color="primary", className="w-100", n_clicks=0),
                        width=4
                    ),
                    dbc.Col(
                        dbc.Button("Access Requests", id="access-requests-tab", color="primary", className="w-100", n_clicks=0),
                        width=4
                    ),
                    dbc.Col(
                        dbc.Button("Roles", id="roles-tab", color="primary", className="w-100", n_clicks=0),
                        width=4
                    ),
                ],
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
                    dbc.Col(html.H5(f"{len(data)} Access Requests"), width="auto", className="mt-4"),
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
                                    html.Td(data["email"]),
                                    html.Td(data["first_name"]),
                                    html.Td(data["last_name"]),
                                    html.Td(data["title"]),  # Assuming "role" in request should be "title" here
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
