import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Function to create figure for a given dataframe
def make_figure(data, title):
    fig = go.Figure()

    # Add temperature line
    fig.add_trace(
        go.Scatter(x=data["date"], y=data["temp"], mode="lines", name=f"{title} Temp",
                   line=dict(color="royalblue"))
    )

    # Update layout for dark theme and styling
    fig.update_layout(
        template="plotly_dark",
        height=400,
        margin=dict(t=40, b=40),
        title=f"Temperature Trends: {title}",
        title_x=0.5,
        title_font=dict(size=20),
        font=dict(size=14),
        paper_bgcolor="black",
        plot_bgcolor="black",
    )

    return fig

# Load the CSV files
day_data = pd.read_csv("./shared_volume/outputs/midelt/day.csv")
month_data = pd.read_csv("./shared_volume/outputs/midelt/month.csv")
year_data = pd.read_csv("./shared_volume/outputs/midelt/year.csv")
year_data = pd.read_csv("./shared_volume/outputs/midelt/year.csv")
max_data = pd.read_csv("./shared_volume/outputs/midelt/max.csv")
min_data = pd.read_csv("./shared_volume/outputs/midelt/min.csv")
saison_data = pd.read_csv("./shared_volume/outputs/midelt/saison.csv")

# Set Streamlit to dark theme and layout
st.set_page_config(page_title="Temperature Dashboard", layout="wide")
st.title("📈 Temperature Data Dashboard")
st.write("An interactive dashboard for visualizing daily, monthly, and yearly temperature data.")

# Create and display figures for each dataset
day_fig = make_figure(day_data, title="Daily")
st.plotly_chart(day_fig, use_container_width=True)

month_fig = make_figure(month_data, title="Monthly")
st.plotly_chart(month_fig, use_container_width=True)

year_fig = make_figure(year_data, title="Yearly")
st.plotly_chart(year_fig, use_container_width=True)

max_fig = make_figure(max_data, title="Temp Max")
st.plotly_chart(max_fig, use_container_width=True)

min_fig = make_figure(min_data, title="Temp Max")
st.plotly_chart(min_fig, use_container_width=True)

saison_fig = make_figure(saison_data, title="Temp Max")
st.plotly_chart(saison_fig, use_container_width=True)

