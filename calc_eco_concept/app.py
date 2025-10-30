import pandas as pd
import numpy as np
from dash import Dash, html, dcc, Input, Output, State, ctx
import plotly.express as px
import os

CSV_PATH = "Ecoconception.csv"

def load_data(csv_path):
    df = pd.read_csv(csv_path, sep=';')
    return df

app = Dash(__name__)


app.layout = html.Div([
    html.H1("Eco-Conception Categorys Map"),
    
    dcc.Graph(id="eco-map", style={"height": "80vh"}),

    html.Div(id="info-panel", style={
        "border": "1px solid #ccc", "padding": "1em", "marginTop": "1em"
    }),

    html.Button("Delete Selected Category", id="delete-btn", n_clicks=0, 
                style={"marginTop": "1em", "backgroundColor": "#e74c3c", "color": "white"}),
    
    dcc.Store(id="selected-id"), 
])

# ---- Callbacks ----
@app.callback(
    Output("eco-map", "figure"),
    Input("delete-btn", "n_clicks"),
    State("selected-id", "data")
)
def update_graph(n_clicks, selected_id):
    df = load_data(CSV_PATH)

    # If delete button pressed, remove the selected item
    if ctx.triggered_id == "delete-btn" and selected_id:
        df = df[df["id"] != selected_id]
        df.to_csv(CSV_PATH, index=False)

    # Prepare layout positions
    if "x" not in df.columns:
        sections = df["Section"].unique()
        mapping = {sec: i for i, sec in enumerate(sections)}
        df["x"] = df["Section"].map(mapping)
        df["y"] = df.groupby("Section").cumcount() + np.random.uniform(-0.4, 0.4, len(df))

    # Create the scatter plot
    fig = px.scatter(
        df,
        x="x", y="y",
        size="Priority",
        color="Lifecycle",
        hover_name="Title",
        hover_data=["Category", "ValidationRules"],
    )
    fig.update_traces(marker=dict(opacity=0.8, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_layout(
        xaxis=dict(showticklabels=False, showgrid=False),
        yaxis=dict(showticklabels=False, showgrid=False),
        plot_bgcolor='white'
    )
    return fig


@app.callback(
    Output("info-panel", "children"),
    Output("selected-id", "data"),
    Input("eco-map", "clickData")
)
def display_info(clickData):
    if clickData:
        point = clickData["points"][0]
        Category = point["hovertext"]
        df = load_data(CSV_PATH)
        row = df[df["Category"] == Category].iloc[0]
        return (
            html.Div([
                html.H3(row["Category"]),
                html.P(f"Description: {row['Description']}"),
                html.P(f"Priority: {row['Priority']}"),
                html.P(f"Lifecycle: {row['Lifecycle']}"),
                html.P(f"Validation Rules: {row['ValidationRules']}"),
            ]),
            int(row["id"])
        )
    return html.Div("Click a Category to view details."), None


if __name__ == "__main__":
    app.run(debug=True)