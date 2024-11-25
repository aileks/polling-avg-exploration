from pathlib import Path

import pandas as pd
import plotly.express as px
from shiny import reactive
from shiny.express import ui, input
from shinywidgets import render_plotly

ui.page_opts(title="2024 Swing State Polling Data", fillable=True)
infile = Path(__file__).parent / "data/swing_polling_pivot_data.csv"
polling_data = pd.read_csv(infile)

with ui.sidebar():
    ui.input_select(
        "state",
        label="Select State",
        choices=polling_data["state"].tolist(),
    )


@reactive.calc
def dat():
    selected_state_data = polling_data[polling_data["state"] == input.state()]
    return selected_state_data


with ui.layout_columns():

    @render_plotly
    def plot1():
        state_data = dat()
        return px.bar(
            state_data,
            x="state",
            y=["Harris", "Trump"],
            barmode="group",
            title=f"Polling Averages for {input.state()}",
            labels={
                "value": "Average Polling Percentage",
                "variable": "Candidate",
                "state": "State",
            },
        )
