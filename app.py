import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(html.H1('POKEDEX'))

pokemon_logo_path = 'https://freepikpsd.com/file/2019/10/png-pokeball-8-1-Transparent-Images-Free.png'
pokemon_logo = html.Img(src = pokemon_logo_path, height = "100vh")
title = html.H1('Pokedex', style ={'fontFamily': 'sans-serif',
                                   'fontSize': '8vh',
                                   'backgroundImage': 'linear-gradient(45deg, #ff9900, #ffffb3)',
                                   'color': 'transparent',
                                   'backgroundClip': 'text',
                                   "WebkitBackgroundClip": "text",
                                   'fontWeight': 'bold'})
search_bar = dbc.Input(id='pokename_input', placeholder = "Search", type='text')
button = dbc.Button('I choose you', id ='i-choose-you', style ={ 'backgroundColor': '#ffe680', 'color': '#000000', 'borderColor': '#ffe680'})

navbar = dbc.Row([dbc.Col(pokemon_logo, width = 1),
                  dbc.Col(title, width = 6),
                  dbc.Col(search_bar, width = 3),
                  dbc.Col(button, width = 2)
                  ], align = 'center', style={'backgroundColor': '#ff4d4d'})

app.layout = dbc.Container(navbar)

if __name__ == '__main__':
    app.run_server(debug=True)