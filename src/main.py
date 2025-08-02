import pandas as pd
from dash import Dash, Input, Output, dcc, html, dash_table, callback
import plotly.express as px
import gui.graphs as graphs

try:
    csv_filepath = './data/maternal_health_risk.csv'
    df = pd.read_csv(csv_filepath)
except FileNotFoundError:
    print(f"Error: The file at {csv_filepath} was not found.")
    df = pd.DataFrame() 

feature_options = ['Age', 'Systolic BP', 'Diastolic', 'BS', 'Body Temp', 'Heart Rate']
graph_options = ['histogram', 'boxplot']

# Initialize the Dash app
app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#111111', 'color': '#FFFFFF', 'fontFamily': 'sans-serif'}, children=[

    # Main Title
    html.Div(style={'textAlign': 'center', 'padding': '20px'}, children=[
        html.H1('Maternal Health Risk Analyzer 🤰')
    ]),

    html.Hr(),

    # Main content area with two columns
    html.Div(className='row', style={'display': 'flex', 'padding': '20px'}, children=[
        html.Div(style={'padding': 10, 'flex': 1}, children=[
            
            # Control for feature selection
            html.H3('Select a Feature'),
            dcc.RadioItems(
                id='feature-controls-and-radio-item',
                options=[{'label': col, 'value': col} for col in feature_options],
                value='Age',
                labelStyle={'display': 'block', 'margin-bottom': '10px'}
            ),
            
            html.Hr(style={'margin': '20px 0'}),

            # Control for graph type
            html.H3('Select Graph Type'),
            dcc.RadioItems(
                id='graph-controls-radio-item', # Corrected ID
                options=[{'label': col.capitalize(), 'value': col} for col in graph_options],
                value='histogram',
                labelStyle={'display': 'block', 'margin-bottom': '10px'}
            )
        ]),

        # --- Right Column (Outputs) ---
        html.Div(style={'padding': 10, 'flex': 2.5}, children=[
            dcc.Graph(
                figure={}, 
                id='health-graph',
                style={'height':'500px'}    
            ),
            
            html.H3('Raw Data', style={'marginTop': '30px'}),
            
            # Data Table
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
                style_table={'borderRadius': '10px', 'overflow': 'hidden'}
            )
        ])
    ])
]) 


@callback(
    Output(component_id='health-graph', component_property='figure'),
    Input(component_id='feature-controls-and-radio-item', component_property='value'),
    Input(component_id='graph-controls-radio-item', component_property='value')
)
def update_graph(col_chosen, graph_type):
    if graph_type == 'histogram':
        fig = graphs.plot_histogram(df, col_chosen)

    elif graph_type == 'boxplot':
        fig = graphs.plot_boxplot(df, col_chosen)

    else:
        fig = {}
        
    return fig


# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)