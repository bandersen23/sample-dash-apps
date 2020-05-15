import dash
from dash.dependencies import Input, Output, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(className='wrapper',
                      children=[
                              dcc.Input(id="input-1", type="number", placeholder="Number 1"),
                              dcc.Input(id="input-2", type="number", placeholder="Number 2"),
                              html.Div(id="number-out-py"),
                              html.Div(id="number-out-js")
                              ])

@app.callback(
    Output("number-out-py", "children"),
    [Input("input-1", "value"), Input("input-2", "value")],
)
def multiply(a,b):
    if a is not None and b is not None:
        answer = a * b
        return f"Server says {a} times {b} is {answer}."
    return None


app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='multiply'
    ),
    Output('number-out-js', 'children'),
    [Input('input-1', 'value'), Input('input-2', 'value')]
)

if __name__ == '__main__':
    app.run_server()
