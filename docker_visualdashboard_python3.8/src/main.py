import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data import getJob_df

print('test')
# print(getJob_df.sort_values("COMPANY_LOC"))
# df = getJob_df.sort_values("COMPANY_LOC").reset_index()
# print(df["COMPANY_LOC"])

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=stylesheets)

# --- pandas dataFrame set start ---

df_test = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [5, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig_test = px.bar(df_test, x="Fruit", y="Amount",
                  color="City", barmode="group")

fig_test.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# figscv = px.line(df, x='AAPL_x', y='AAPL_y',
#                  title='Apple Share Prices over time (2014)')

# --- pandas dataFrame set end ---


# --- pandas dataFrame set start ---
# Read data from a csv
z_data = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig_test001 = go.Figure(data=[go.Surface(z=z_data.values)])
fig_test001.update_traces(contours_z=dict(show=True, usecolormap=True,
                                          highlightcolor="limegreen", project_z=True))
fig_test001.update_layout(title='TEST', autosize=False,
                          scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                          width=1000, height=600,
                          margin=dict(l=65, r=50, b=65, t=90)
                          )

fig_test001.show()
# --- pandas dataFrame set end ---


# --- pandas dataFrame set start ---
fig_test002 = go.Figure(go.Sunburst(
    ids=[
        "North America", "Europe", "Australia", "North America - Football", "Soccer",
        "North America - Rugby", "Europe - Football", "Rugby",
        "Europe - American Football", "Australia - Football", "Association",
        "Australian Rules", "Autstralia - American Football", "Australia - Rugby",
        "Rugby League", "Rugby Union"
    ],
    labels=[
        "North<br>America", "Europe", "Australia", "Football", "Soccer", "Rugby",
        "Football", "Rugby", "American<br>Football", "Football", "Association",
        "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
        "Rugby<br>Union"
    ],
    parents=[
        "", "", "", "North America", "North America", "North America", "Europe",
        "Europe", "Europe", "Australia", "Australia - Football", "Australia - Football",
        "Australia - Football", "Australia - Football", "Australia - Rugby",
        "Australia - Rugby"
    ],
))
fig_test002.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig_test002.show()
# --- pandas dataFrame set end ---

# --- pandas dataFrame set start ---
df_test003 = px.data.iris()  # iris is a pandas DataFrame
fig_test003 = px.scatter(df_test003, x="sepal_width", y="sepal_length")
# --- pandas dataFrame set end ---

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

        # html.Div(
        #     style={"textAlign": "center", "paddingTop": "20px"},
        #     children=[
        #         dcc.Input(placeholder="Search Code?",
        #                   id="search_countries"),
        #         html.H2(children="Hello anonymous", id="output_countries"),
        #     ]
        # ),

        # dcc.Graph(
        #     id='example-graph-2',
        #     figure=fig_test
        # ),

        dcc.Graph(
            # id='example-graph-001',
            figure=fig_test001
        ),

        dcc.Graph(
            # id='example-graph-002',
            figure=fig_test002
        ),

        dcc.Graph(
            # id='example-graph-002',
            figure=fig_test003
        ),


    ],
)


@app.callback(Output("hello-output", "children"), [Input("hello-input", "value")])
def update_hello(value):
    if value is None:
        return "Not CODE"
    else:
        return f"CODE : {value}"


# @app.callback(Output("output_countries", "children"), [Input("search_countries", "value")])
# def update_hello(value):
#     if value is None:
#         return "Not CODE"
#     else:
#         return f"CODE : {value}"


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050)
