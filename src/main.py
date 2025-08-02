import pandas as pd
from dash import Dash, Input, Output, dcc, html, dash_table, callback
import plotly.express as px
import gui.graph_builder as graph_builder
from gui.components.data_table import data_table
from gui.components.dist_graph import dist_graph
from gui.components.feature_comp_graph import feature_comp_graph


try:
    csv_filepath = './data/maternal_health_risk.csv'
    df = pd.read_csv(csv_filepath)
except FileNotFoundError:
    print(f"Error: The file at {csv_filepath} was not found.")
    df = pd.DataFrame() 

feature_options = ['Age', 'Systolic BP', 'Diastolic', 'BS', 'Body Temp', 'Heart Rate']
dist_graph_options = ['histogram', 'boxplot']
comp_graph_options = ['scatter_matrix']

# Initialize the Dash app
app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#111111', 'color': '#FFFFFF', 'fontFamily': 'sans-serif'}, children=[

    # Main Title
    html.Div(style={'textAlign': 'center', 'padding': '20px'}, children=[
        html.H1('Maternal Health Risk Analyzer 🤰')
    ]),

    html.Hr(),

    data_table(df, feature_options),

    # graph area with two columns
    dist_graph(feature_options, dist_graph_options),
    feature_comp_graph(feature_options, comp_graph_options)
])

@callback(
    Output(component_id='dist-graph', component_property='figure'),
    Input(component_id='feature-dist-graph-radio-item', component_property='value'),
    Input(component_id='graph-dist-graph-radio-item', component_property='value')
)
# input arguments are currentr value of each input properties, IN THE ORDER THEY WERE SPECIFIED
def update_dist_graph(dist_col, graph_type):
    if graph_type == 'histogram':
        fig = graph_builder.plot_histogram(df, dist_col)

    elif graph_type == 'boxplot':
        fig = graph_builder.plot_boxplot(df, dist_col)

    else:
        fig = {}
        
    return fig

@callback(
        Output(component_id='feature-comparison-graph', component_property='figure'),
        Input(component_id='xfeature-comparison-graph', component_property='value'),
        Input(component_id='yfeature-comparison-graph', component_property='value'),
        Input(component_id='comparison-graph-radio-item', component_property='value')
)
def update_comparison_graph(x_col, y_col, graph_type):
    if graph_type == 'scatter_matrix':
        fig = graph_builder.plot_scatter_matrix(df, x_col, y_col)
    else:
        fig = {}

    return fig


@callback(
    Output(component_id='mean-value', component_property='children'),
    Output(component_id='median-value', component_property='children'),
    Output(component_id='mode-value', component_property='children'),
    Input(component_id='metrics-feature-dropdown', component_property='value')
)
def update_metrics(selected_feature):
    if selected_feature:
        mean_val = df[selected_feature].mean()
        median_val = df[selected_feature].median()
        mode_val = df[selected_feature].mode()
        
        formatted_mean = f'{mean_val:.2f}'
        formatted_median = f'{median_val:.2f}'
        if not mode_val.empty:
            formatted_mode = f'{mode_val.iloc[0]:.2f}'
        else:
            formatted_mode = '-'
        
        return formatted_mean, formatted_median, formatted_mode
    
    return '-', '-', '-'



# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)