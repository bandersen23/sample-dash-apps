import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_color_picker as dcp
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(className='wrapper',
                      children=[html.H1(id='hello',children='This will change color'),
                                dcp.ColorPicker(id='coloring', color='blue')])

@app.callback(Output('hello', 'style'), [Input('coloring', 'color')])
def update_color(color):
    return {'color':color}

if __name__ == '__main__':
    app.run_server()
