import pandas as pd
from dash import Dash, Input, Output, dcc, html, dash_table, callback

def dist_graph(feature_options, graph_options):
    return (
        # graph area with two columns
        html.Div(className='row', style={'display': 'flex', 'padding': '20px'}, children=[
            html.Div(style={'padding': 10, 'flex': 1}, children=[
                # feature selection
                html.H2('Distribution Analysis'),
                html.H3('Select a Feature'),
                dcc.RadioItems(
                    id='feature-dist-graph-radio-item',
                    options=[{'label': col, 'value': col} for col in feature_options],
                    value='Age',
                    labelStyle={'display': 'block', 'margin-bottom': '10px'}
                ),
                
                html.Hr(style={'margin': '20px 0'}),

                # Control for graph type
                html.H3('Select Graph Type'),
                dcc.RadioItems(
                    id='graph-dist-graph-radio-item', # Corrected ID
                    options=[{'label': col.capitalize(), 'value': col} for col in graph_options],
                    value='histogram',
                    labelStyle={'display': 'block', 'margin-bottom': '10px'}
                )
            ]),
            html.Div(style={'padding': 10, 'flex': 2.5}, children=[
                dcc.Graph(
                    figure={}, 
                    id='dist-graph',
                    style={'height':'500px'}    
                )
            ])
        ])
    )