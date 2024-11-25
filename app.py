from pathlib import Path

import pandas as pd
import plotly.express as px
from shiny import reactive
from shiny.express import ui, input
from shinywidgets import render_plotly

ui.page_opts(
    title="2024 Swing State Polling Data",
    fillable=True,
    page_navbar=True,
)
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


with ui.div(class_="d-flex justify-content-center w-100"):
    with ui.layout_columns():

        @render_plotly
        def plot():
            state_data = dat()
            fig = px.bar(
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

            fig.update_layout(
                autosize=True,
                width=1000,
                height=800,
                margin=dict(l=50, r=50, t=50, b=50),
            )
            return fig
