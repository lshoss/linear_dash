import plotly.express as px

# define function that receives graph type and plots it based on columns 

def plot_histogram(df, x_column):
    fig = px.histogram(
        df,
        x = x_column,
        # y=y_column,
        color = 'Risk Level',
        barmode='group',      # Groups the bars side-by-side
        title=f'Distribution of {x_column} by Risk Level',
        template='plotly_dark', # A nice dark theme for better visibility
        color_discrete_map={ # Optional: Define your own colors
             'low risk': '#1f77b4',
             'mid risk': '#ff7f0e',
             'high risk': '#d62728'
        }
    )
    fig.update_layout(
        xaxis_title=x_column,
        yaxis_title='Count of Patients',
        legend_title_text='Risk Level'
    )
    return fig

def plot_boxplot(df, y_column):
    fig = px.box(
        df,
        y=y_column,
        color='Risk Level', # Ensure this column name matches your DataFrame
        title=f'Distribution of {y_column} by Risk Level',
        template='plotly_dark',
        color_discrete_map={
             'low risk': '#1f77b4',
             'mid risk': '#ff7f0e',
             'high risk': '#d62728'
        }
    )
    fig.update_layout(
        yaxis_title=y_column,
        legend_title_text='Risk Level'
    )
    return fig