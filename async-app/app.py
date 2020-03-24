import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import aiohttp
import asyncio
import async_timeout
from bs4 import BeautifulSoup

loop = asyncio.get_event_loop()
app = dash.Dash()

async def fetch_status(url):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get(url) as response:
            return response.status

async def fetch_text(url):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

def query(qtype = 'status', loop=None):
    asyncio.set_event_loop(loop)
    if qtype == 'status':
    
        responses = loop.run_until_complete(asyncio.gather(
            fetch_status("https://google.com/"),
            fetch_status("https://bing.com/"),
            fetch_status("https://duckduckgo.com"),
            fetch_status("http://www.yahoo.com"),
        ))
    
    elif qtype == 'text':
        responses = loop.run_until_complete(asyncio.gather(
            fetch_text("https://www.google.com"),
            fetch_text("https://bing.com/"),
            fetch_text("https://duckduckgo.com"),
            fetch_text("http://www.yahoo.com"),
        ))
        
    else:
        responses = 'Not an option'
    
    return responses


def process_html(res):
    
    try:
        soup = BeautifulSoup(res, 'html.parser')
        title = soup.find('title').text
    except: 
        title = "Cannot Find It"
    return title


app.layout = html.Div([
    html.Button('Click Me', id='button'),
    html.H3(id='button-clicks'),
    dcc.Markdown(id='response-status')])

@app.callback(
    Output('response-status', 'children'),
    [Input('button', 'n_clicks')])
def clicks(n_clicks):
    if n_clicks is not None:
        
        # make a query
        res = query(qtype='text', loop=loop)
        
        # do something with the query
        # in this case I'm just processing the text to Markdown
        text = [f"Webpage Title: {process_html(x)}  " for x in res]
        
        return text

if __name__ == '__main__':
    app.run_server(use_reloader=False)