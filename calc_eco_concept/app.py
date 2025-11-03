import pandas as pd
import numpy as np
import random
from dash import Dash, html, dcc, Input, Output, State, ctx
import plotly.express as px
import os
import shutil

# File paths
CSV_PATH = "C:\\Users\\ambroise\\Documents\\GitHub\\draft_ambroise\\calc_eco_concept\\Ecoconception.csv"
CSV_COPY_PATH = "C:\\Users\\ambroise\\Documents\\GitHub\\draft_ambroise\\calc_eco_concept\\Ecoconception_copy.csv"
CSV_TEMP_PATH = "C:\\Users\\ambroise\\Documents\\GitHub\\draft_ambroise\\calc_eco_concept\\Ecoconception_temp.csv"

# Create a copy of the original CSV file if the first copy doesn't exist
if not os.path.exists(CSV_COPY_PATH):
    shutil.copy(CSV_PATH, CSV_COPY_PATH)

# Create a temporary copy for modifications
shutil.copy(CSV_COPY_PATH, CSV_TEMP_PATH)

def load_data(csv_path):
    df = pd.read_csv(csv_path, sep=';')
    df["id"] = df.index + 1  # Start the id from 1 (change to 0 if you prefer)
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

    html.Button("Validate Changes", id="validate-btn", n_clicks=0, 
                style={"marginTop": "1em", "backgroundColor": "#2ecc71", "color": "white"}),

    html.Button("Reset Changes", id="reset-btn", n_clicks=0, 
                style={"marginTop": "1em", "backgroundColor": "#3498db", "color": "white"}),

    dcc.Store(id="selected-id"), 
])

# ---- Callbacks ----
@app.callback(
    Output("eco-map", "figure"),
    Input("delete-btn", "n_clicks"),
    Input("validate-btn", "n_clicks"),
    Input("reset-btn", "n_clicks"),  # Add reset button input
    State("selected-id", "data")
)
def update_graph(delete_clicks, validate_clicks, reset_clicks, selected_id):
    # If reset button is pressed, restore the temporary copy from the first copy
    if ctx.triggered_id == "reset-btn":
        shutil.copy(CSV_COPY_PATH, CSV_TEMP_PATH)  # Restore the temporary copy
        df = load_data(CSV_TEMP_PATH)  # Reload the restored copy
    else:
        # Load the temporary copy of the CSV
        df = load_data(CSV_TEMP_PATH)

    # If delete button pressed, remove the selected item from the temporary copy
    if ctx.triggered_id == "delete-btn" and selected_id:
        df = df[df["id"] != selected_id]
        df.to_csv(CSV_TEMP_PATH, index=False, sep=';')

    # If validate button pressed, save the temporary copy to the first copy
    if ctx.triggered_id == "validate-btn":
        shutil.copy(CSV_TEMP_PATH, CSV_COPY_PATH)

    # Create y-axis positions based on Priority, Lifecycle, and Category
    if "x" not in df.columns or "y" not in df.columns:
        # Assign y positions based on Priority, Lifecycle, and Category
        priority_levels = sorted(df["Priority"].unique(), reverse=False)  # Higher priority at the top
        lifecycle_levels = {lifecycle: i for i, lifecycle in enumerate(sorted(df["Lifecycle"].unique()))}
        category_levels = {category: i for i, category in enumerate(sorted(df["Category"].unique()))}
        section_order = {section: i for i, section in enumerate(sorted(df["Section"].unique()))}

        y_positions = []
        x_positions = []
        for _, row in df.iterrows():
            # Calculate y position: Priority determines the main section, Lifecycle and Category refine it
            priority_index = priority_levels.index(row["Priority"])
            lifecycle_index = lifecycle_levels[row["Lifecycle"]]
            category_index = category_levels[row["Category"]]

            # Combine indices to create a unique y position
            y = priority_index * 108 + (category_index * 12 + 6)

            # Calculate x position: Section determines the main x position
            x = section_order[row["Section"]] * 250 + 125  # Double the x-axis width
            i = 1
            # Ensure no overlap by slightly adjusting x if the same y already exists
            while (x, y) in zip(x_positions, y_positions):
                x += i*15 
                # Slightly adjust x to avoid overlap
                if (x, y) in zip(x_positions, y_positions):
                    i += 1 
                    x -= i*15
                i += 1
            y_positions.append(y)
            x_positions.append(x)

        # Assign x and y positions to the DataFrame
        df["x"] = x_positions
        df["y"] = y_positions

    # Create the scatter plot
    df["size"] = 100  # Fixed size for all points
    fig = px.scatter(
        df,
        x="x", y="y",
        size="size",
        size_max=5,
        color="Lifecycle",
        hover_name="Title",
        hover_data=["ValidationRules"],
    )
    fig.update_traces(
        customdata=df[["Title", "ValidationRules"]],  # Add Title and ValidationRules as custom data
        hovertemplate="<b>Title:</b> %{customdata[0]}<br>" +  # Display Title
                      "<b>Validation Rules:</b> %{customdata[1]}<br>" +  # Display ValidationRules
                      "<extra></extra>"  # Remove the default trace info
    )

    # Add shadow lines for Priority levels
    for i, priority in enumerate(priority_levels):
        y_start = i * 108 
        fig.add_shape(
            type="line",
            x0=0, x1=len(df["Section"].unique()) * 250,  # Adjusted for double x-axis width
            y0=y_start, y1=y_start,
            line=dict(color="LightGray", width=1, dash="dot")  # Shadow line style
        )

    # Add shadow lines for Category within each Priority
    for i, priority in enumerate(priority_levels):
        for j, category in enumerate(category_levels):
            y_start = i * 108 + j * 12 
            fig.add_shape(
                type="line",
                x0=0, x1=len(df["Section"].unique()) * 250,  # Adjusted for double x-axis width
                y0=y_start, y1=y_start,
                line=dict(color="Gainsboro", width=0.5, dash="dot")
            )
            # Add category labels as a sub-legend
            fig.add_annotation(
                x=-50,  # Place the label outside the plot area
                y=y_start + 6,  # Center the label within the category block
                text=f" {category}",
                showarrow=False,
                font=dict(size=10, color="Gray"),
                align="right",
            )

    # Add vertical lines for each Section
    for i, section in enumerate(sorted(df["Section"].unique())):
        fig.add_shape(
            type="line",
            x0=i * 250, x1=i * 250,  # Adjusted for double x-axis width
            y0=0, y1=max(y_positions)+20,
            line=dict(color="LightGray", width=1, dash="dot")
        )

    # Update layout to show x-axis and y-axis labels
    fig.update_layout(
        yaxis=dict(
            title="Priority / Lifecycle / Category",
            tickvals=[i * 108 + 54 for i in range(len(priority_levels))],
            ticktext=[f"Priority {p}" for p in priority_levels],
            showgrid=False,  # Disable default gridlines
        ),
        xaxis=dict(
            title="Section",
            tickvals=[i * 250 + 125 for i in range(len(section_order))],  # Adjusted for double x-axis width
            ticktext=list(section_order.keys()),  # Show section names as x-axis labels
            showgrid=False,  # Disable default gridlines
        ),
        plot_bgcolor='white',
        legend_title="Lifecycle",  # Add a clear legend title
    )

    # Adjust text position to appear below the points
    fig.update_traces(
        textposition="bottom center"  # Position the text below the points
    )

    return fig


@app.callback(
    Output("info-panel", "children"),
    Output("selected-id", "data"),
    Input("reset-btn", "n_clicks"),
    Input("eco-map", "clickData")
)
def display_info(clickData):
    if clickData:
        point = clickData["points"][0]
        Title = point["hovertext"]
        df = load_data(CSV_TEMP_PATH)

        # Filter the DataFrame for the selected Title
        filtered_df = df[df["Title"] == Title]
        
        # Check if the filtered DataFrame is empty
        if not filtered_df.empty:
            row = filtered_df.iloc[0]  # Safely access the first row
            return (
                html.Div([
                    html.H3(row["Title"]),
                    html.H4(row["Category"]),
                    html.P(f"Priority: {row['Priority']}"),
                    html.P(f"Lifecycle: {row['Lifecycle']}"),
                    html.P(f"Validation Rules: {row['ValidationRules']}"),
                    html.P(f"Section: {row['Section']}"),
                ]),
                int(row["id"])
            )
        else:
            return html.Div("No data found for the selected category."), None

    return html.Div("Click a Category to view details."), None


if __name__ == "__main__":
    app.run(debug=True)