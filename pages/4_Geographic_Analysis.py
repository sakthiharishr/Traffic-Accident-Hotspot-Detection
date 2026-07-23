import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

st.title("🌍 Geographic Analysis")

df = load_data()

city_stats = (
    df.groupby("city")
    .size()
    .reset_index(name="accidents")
    .sort_values(
        "accidents",
        ascending=False
    )
)

st.subheader(
    "Top Accident-Prone Cities"
)

st.dataframe(
    city_stats,
    use_container_width=True
)

fig = px.bar(
    city_stats,
    x="city",
    y="accidents",
    title="Accidents by City"
)

st.plotly_chart(
    fig,
    use_container_width=True
)