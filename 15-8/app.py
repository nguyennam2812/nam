from dash import Dash, html, dcc, no_update
from dash.dependencies import Input, Output, State
import pandas as pd
import request
from confirmation import create_confirmation_page

# Khởi tạo ứng dụng Dash
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=['assets/styles.css'])

# Nội dung trang chính
home_page = html.Div(
    className='home-request-page',
    children=[
        html.Div(
            className='home-request-page-container',
            children=[
                html.H1(children="Log in to Fora"),
                html.Button(children="Continue with SSO", className="button button-primary"),
                html.Button(children="Request Access", id='request-access-button', className="button button-secondary")
            ]
        )
    ]
)

# Nội dung trang yêu cầu truy cập từ request.py
request_access_page = html.Div(
    className='home-request-page',
    children=[
        html.Div(
            className='home-request-page-container',
            children=request.create_request_page().children
        )
    ]
)

# Định nghĩa layout với các trang khác nhau
app.layout = html.Div(
    className="container",
    children=[
        dcc.Location(id='url', refresh=False),  # Xử lý thay đổi URL mà không làm mới trang
        dcc.Store(id='form-data', storage_type='session'),  # Lưu trữ dữ liệu trong session
        html.Div(id='page-content')  # Chứa nội dung của các trang động
    ]
)

# Callback để cập nhật nội dung dựa trên URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')],
    [State('form-data', 'data')]
)
def display_page(pathname, data):
    if pathname == '/' or pathname is None:
        return home_page
    elif pathname == '/request-access':
        return request_access_page
    elif pathname == '/confirmation':
        if data:
            return create_confirmation_page(data)
        return home_page
    else:
        return home_page

# Kết hợp các callback để cập nhật URL
@app.callback(
    Output('url', 'pathname'),
    [Input('request-access-button', 'n_clicks'),
     Input('submit-button', 'n_clicks')],
    [State('form-data', 'data')],
    prevent_initial_call=True
)
def update_url(request_clicks, submit_clicks, data):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return no_update
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if trigger_id == 'request-access-button' and request_clicks:
        return '/request-access'
    elif trigger_id == 'submit-button' and submit_clicks and data:
        # Lưu dữ liệu form vào file CSV
        df = pd.DataFrame([data])
        try:
            old_data = pd.read_csv('form_data.csv')
            df = pd.concat([old_data, df], ignore_index=True)
        except FileNotFoundError:
            pass
        df.to_csv('form_data.csv', index=False)
        return '/confirmation'
    
    return no_update

# Thêm các callback từ module request
request.add_request_callback(app)

# Chạy server
if __name__ == "__main__":
    app.run_server(debug=True)
