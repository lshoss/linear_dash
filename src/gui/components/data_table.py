import pandas as pd
from dash import Dash, Input, Output, dcc, html, dash_table, callback

def data_table(df, feature_options):
    return (
        html.Div(className='metrics-data-row', style={'display': 'flex', 'padding': '20px', 'alignItems': 'stretch'}, children=[
            # Metrics table
            html.Div(style = {'padding': 10, 'flex': 1}, children = [
                # Title for the metrics section
                html.H3('Dataset Metrics'),
                # Dropdown to select a feature
                dcc.Dropdown(
                    id = 'metrics-feature-dropdown',
                    options = feature_options,
                    value = 'Age',
                    clearable = False,
                    style = {
                        'color': 'black',
                        'marginBottom': '20px'
                    }
                ),
                # Container for displaying the metrics of the selected feature
                html.Div(id='metrics-display', children=[
                    html.Div([
                        html.H5('Mean', style={'fontWeight': 'bold', 'color': '#CCCCCC'}),
                        html.P(id='mean-value', children=['-'], style={'color': '#AAAAAA'})
                    ], style={'backgroundColor': '#222222', 'padding': '10px', 'border': '1px solid #444444', 'borderRadius': '5px', 'marginBottom': '10px'}),
                    
                    html.Div([
                        html.H5('Median', style={'fontWeight': 'bold', 'color': '#CCCCCC'}),
                        html.P(id='median-value', children=['-'], style={'color': '#AAAAAA'})
                    ], style={'backgroundColor': '#222222', 'padding': '10px', 'border': '1px solid #444444', 'borderRadius': '5px', 'marginBottom': '10px'}),
                    
                    html.Div([
                        html.H5('Mode', style={'fontWeight': 'bold', 'color': '#CCCCCC'}),
                        html.P(id='mode-value', children=['-'], style={'color': '#AAAAAA'})
                    ], style={'backgroundColor': '#222222', 'padding': '10px', 'border': '1px solid #444444', 'borderRadius': '5px'})
                ])
            ]),
            # Data Table Column - This section is styled to ensure even height
            html.Div(style={'padding': 10, 'flex': 2.5, 'display': 'flex', 'flexDirection': 'column'}, children = [
                html.H3('Raw Data', style={'flex': 'none', 'marginBottom': '15px'}),
                # Wrapper div to allow the DataTable to grow
                html.Div(style={'flex': '1 1 auto', 'display': 'flex', 'flexDirection': 'column'}, children=[
                    dash_table.DataTable(
                        id='data-table',
                        data=df.to_dict('records'),
                        page_size=8,
                        style_header={
                            'backgroundColor': 'rgb(30, 30, 30)',
                            'color': 'white',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'backgroundColor': 'rgb(50, 50, 50)',
                            'color': 'white',
                            'textAlign': 'left',
                            'padding': '10px',
                            'border': '1px solid #444444'
                        },
                        style_table={
                            'borderRadius': '10px', 
                            'overflow': 'hidden',
                            'height': '100%' # Ensures the table fills its container
                        },
                        style_as_list_view=True,
                    )
                ])
            ])
        ])
    )