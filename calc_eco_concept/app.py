import pandas as pd
import numpy as np
import random
from dash import Dash, html, dcc, Input, Output, State, ctx
import plotly.express as px
import os

CSV_PATH = "C:\\Users\\ambroise\\Documents\\GitHub\\draft_ambroise\\calc_eco_concept\\Ecoconception.csv"

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

    # Create y-axis positions based on Priority, Lifecycle, and Category
    if "x" not in df.columns or "y" not in df.columns:
        # Assign y positions based on Priority, Lifecycle, and Category
        priority_levels = sorted(df["Priority"].unique(), reverse=False)  # Higher priority at the top
        lifecycle_levels = {lifecycle: i for i, lifecycle in enumerate(sorted(df["Lifecycle"].unique()))}
        category_levels = {category: i for i, category in enumerate(sorted(df["Category"].unique()))}
        sections_levels = {section: i for i, section in enumerate(sorted(df["Section"].unique()))}
       

        y_positions = []
        for _, row in df.iterrows():
            # Calculate y position: Priority determines the main section, Lifecycle and Category refine it
            priority_index = priority_levels.index(row["Priority"])
            lifecycle_index = lifecycle_levels[row["Lifecycle"]]
            category_index = category_levels[row["Category"]]

            # Combine indices to create a unique y position
            y = priority_index * 100 + lifecycle_index * 10 + category_index
            y_positions.append(y)

        # Assign x positions based on Section
        section_order = {section: i for i, section in enumerate(sorted(df["Section"].unique()))}
        df["x"] = df["Section"].map(section_order)  # Map sections to sequential x positions
        df["y"] = y_positions

    # Create the scatter plot
    df["size_adjusted"] = df["Priority"] * 1
    fig = px.scatter(
        df,
        x="x", y="y",
        size="size_adjusted",
        size_max=15,
        color="Lifecycle",
        hover_name="Title",
        hover_data=["Category", "ValidationRules", "Section", "Priority"],
    )

    # Add shadow lines for Priority levels
    for i, priority in enumerate(priority_levels):
        y_start = i * 100
        fig.add_shape(
            type="line",
            x0=0, x1=len(df["Section"].unique()),  # Full width of the plot
            y0=y_start, y1=y_start,
            line=dict(color="LightGray", width=1, dash="dot")  # Shadow line style
        )

    # Add shadow lines for Lifecycle within each Priority
    for i, priority in enumerate(priority_levels):
        for j in range(len(lifecycle_levels)):
            y_start = i * 100 + j * 10
            fig.add_shape(
                type="line",
                x0=0, x1=len(df["Section"].unique()),
                y0=y_start, y1=y_start,
                line=dict(color="Gainsboro", width=0.5, dash="dot")
            )

    # Add vertical lines for each Section
    for i, section in enumerate(sorted(df["Section"].unique())):
        fig.add_shape(
            type="line",
            x0=i, x1=i,
            y0=0, y1=max(y_positions),
            line=dict(color="LightGray", width=1, dash="dot")
        )

    # Update layout to show x-axis and y-axis labels
    fig.update_layout(
        yaxis=dict(
            title="Priority / Lifecycle / Category",
            tickvals=[i * 100 for i in range(len(priority_levels))],
            ticktext=[f"Priority {p}" for p in priority_levels],
            showgrid=False,  # Disable default gridlines
        ),
        xaxis=dict(
            title="Section",
            tickvals=list(range(len(section_order))),
            ticktext=list(section_order.keys()),  # Show section names as x-axis labels
            showgrid=False,  # Disable default gridlines
        ),
        plot_bgcolor='white',
        legend_title="Lifecycle",  # Add a clear legend title
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
                html.P(f"Section: {row['Section']}"),
            ]),
            int(row["id"])
        )
    return html.Div("Click a Category to view details."), None


if __name__ == "__main__":
    app.run(debug=True)