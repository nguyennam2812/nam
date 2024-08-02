from dash import html, dcc
from dash.dependencies import Input, Output, State

# Hàm tạo trang yêu cầu truy cập
def create_request_page():
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Label("First Name *", className="label-field"),
                    dcc.Input(type="text", id="first-name", required=True, className="input-field")
                ],
                style={'display': 'inline-block', 'width': '48%', 'margin-right': '4%'}
            ),
            
            html.Div(
                children=[
                    html.Label("Last Name *", className="label-field"),
                    dcc.Input(type="text", id="last-name", required=True, className="input-field")
                ],
                style={'display': 'inline-block', 'width': '48%'}
            ),
            
            html.Label("Email Address *", className="label-field"),
            dcc.Input(type="email", id="email", required=True, className="input-field"),
            
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Label("Title *", className="label-field"),
                            dcc.Input(type="text", id="title", required=True, className="input-field")
                        ],
                        style={'display': 'inline-block', 'width': '45%', 'margin-right': '5%'}
                    ),
                    
                    html.Div(
                        children=[
                            html.Label("Function *", className="label-field"),
                            dcc.Dropdown(
                                id="function",
                                options=[
                                    {'label': 'Option 1', 'value': 'option1'},
                                    {'label': 'Option 2', 'value': 'option2'},
                                    {'label': 'Option 3', 'value': 'option3'}
                                ],
                                className="input-field"
                            )
                        ],
                        style={'display': 'inline-block', 'width': '45%'}
                    )
                ],
                style={'display': 'flex', 'width': '100%'}
            ),
            
            html.Button("Request Access", id="submit-button", className="button button-primary", type="submit")
        ]
    )

# Callback để xử lý khi nhấn nút "Request Access"
def add_request_callback(app):
    @app.callback(
        Output('form-data', 'data'),
        [Input('submit-button', 'n_clicks')],
        [
            State('first-name', 'value'),
            State('last-name', 'value'),
            State('email', 'value'),
            State('title', 'value'),
            State('function', 'value')
        ]
    )
    def save_form_data(n_clicks, first_name, last_name, email, title, function):
        if n_clicks:
            return {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'title': title,
                'function': function
            }
        return {}

    @app.callback(
        Output('url', 'pathname', allow_duplicate=True),
        [Input('form-data', 'data')],
        prevent_initial_call=True
    )
    def submit_request(data):
        if data:
            return '/confirmation'
        return '/request-access'

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dữ liệu mẫu
users = [
    {'email': 'aly.meixell@orionworldwide.com', 'first_name': 'Aly', 'last_name': 'Meixell', 'role': 'User', 'status': 'Inactive'},
    {'email': 'kimberly.housley@orionworldwide.com', 'first_name': 'Kimberly', 'last_name': 'Housley', 'role': 'User', 'status': 'Inactive'}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    role = request.form['role']
    status = request.form['status']
    users.append({'email': email, 'first_name': first_name, 'last_name': last_name, 'role': role, 'status': status})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
