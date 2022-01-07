import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from data import countries_df


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=stylesheets)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# dfScv = pd.read_csv("data/jobs.csv")
# dfscv = pd.read_csv(
#     'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

# print(dfscv)

# figscv = px.line(df, x='AAPL_x', y='AAPL_y',
#                  title='Apple Share Prices over time (2014)')

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={"textAlign": "center", "paddingTop": "50px"},
            children=[html.H1("Cleancode Dashboard", style={"fontSize": 40})],
        ),
        # html.Div(children='Dash: A web application framework for Python.', style={
        #     'textAlign': 'center',
        #     'color': colors['text']
        # }),
        html.Div(
            style={"textAlign": "center", "paddingTop": "20px"},
            children=[
                dcc.Input(placeholder="Search Code?",
                          id="hello-input"),
                html.H2(children="Hello anonymous", id="hello-output"),
            ]
        ),

        dcc.Graph(
            id='example-graph-2',
            figure=fig
        )
    ],
)


@app.callback(Output("hello-output", "children"), [Input("hello-input", "value")])
def update_hello(value):
    if value is None:
        return "Not CODE"
    else:
        return f"CODE : {value}"


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050)
