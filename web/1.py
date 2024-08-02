from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import request
import dash

# Khởi tạo ứng dụng Dash với suppress_callback_exceptions và CSS bên ngoài
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=['assets/styles.css'])

# Nội dung trang chính
home_page = html.Div(
    children=[
        html.H1(children="Log in to Fora"),
        html.Button(children="Continue with SSO", className="button button-primary"),
        html.Button(children="Request Access", id='request-access-button', className="button button-secondary")  # Đảm bảo nút này có ID đúng
    ]
)

# Nội dung trang yêu cầu truy cập từ request.py
request_access_page = request.create_request_page()

# Nội dung trang xác nhận
confirmation_page = html.Div(
    children=[
        html.H1("Access Requested"),
        html.P("Thank you for requesting access. We will get back to you soon.")
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
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/request-access':
        return request_access_page
    elif pathname == '/confirmation':
        return confirmation_page
    else:
        return home_page

# Callback để cập nhật URL dựa trên nhấn nút hoặc dữ liệu biểu mẫu
@app.callback(
    Output('url', 'pathname'),
    [Input('request-access-button', 'n_clicks'),  # Đảm bảo ID đúng
     Input('form-data', 'data')],
    prevent_initial_call=True
)
def update_url(n_clicks, data):
    ctx = dash.callback_context
    if not ctx.triggered:
        return '/'
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if trigger_id == 'request-access-button' and n_clicks is not None:
        return '/request-access'
    elif trigger_id == 'form-data' and data:
        return '/confirmation'
    
    return '/'

# Thêm các callback từ module request
request.add_request_callback(app)

# Chạy server
if __name__ == "__main__":
    app.run_server(debug=True)
