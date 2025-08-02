import pandas as pd
from dash import Dash, Input, Output, dcc, html, dash_table, callback

def feature_comp_graph(feature_options, graph_options):
    return (
        # graph area with two columns
        html.Div(className='row', style={'display': 'flex', 'padding': '20px'}, children=[
            html.Div(style={'padding': 10, 'flex': 1}, children=[
                # feature selection
                html.H2('Feature Relation Analysis'),
                html.Div(children=[
                    html.H3('Select X-axis Feature'),
                    dcc.RadioItems(
                        id='xfeature-comparison-graph',
                        options=[{'label': col, 'value': col} for col in feature_options],
                        value='Age',
                        labelStyle={'display': 'block', 'margin-bottom': '10px'}
                    ),

                    html.Hr(),

                    html.H3('Select Y-axis Feature'),
                    dcc.RadioItems(
                        id='yfeature-comparison-graph',
                        options=[{'label': col, 'value': col} for col in feature_options],
                        value='Body Temp',
                        labelStyle={'display': 'block', 'margin-bottom': '10px'}
                    )
                ]),

                html.Hr(style={'margin': '20px 0'}),

                # Control for graph type
                html.H3('Select Graph Type'),
                dcc.RadioItems(
                    id='comparison-graph-radio-item', # Corrected ID
                    options=[{'label': col.capitalize(), 'value': col} for col in graph_options],
                    value='scatter_matrix',
                    labelStyle={'display': 'block', 'margin-bottom': '10px'}
                )
            ]),
            html.Div(style={'padding': 10, 'flex': 2.5}, children=[
                dcc.Graph(
                    figure={}, 
                    id='feature-comparison-graph',
                    style={'height':'500px'}    
                )
            ])
        ])
    )