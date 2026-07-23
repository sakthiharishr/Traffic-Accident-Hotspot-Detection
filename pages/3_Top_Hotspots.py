import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.hotspot_detection import detect_hotspots
from utils.hotspot_ranking import get_top_hotspots

st.title("🔥 Top Hotspots")

df = load_data()

selected_city = st.selectbox(
    "Select City",
    sorted(df["city"].unique())
)

city_df = df[
    df["city"] == selected_city
]

city_df = detect_hotspots(city_df)

st.subheader("Cluster Distribution")
st.write(city_df["cluster"].value_counts())

hotspots = get_top_hotspots(city_df)

if len(hotspots) == 0:

    st.warning(
        "No hotspots detected."
    )

else:

    st.dataframe(
        hotspots[
            [
                "hotspot_id",
                "accidents",
                "avg_risk"
            ]
        ],
        use_container_width=True
    )

    fig = px.bar(
        hotspots,
        x="hotspot_id",
        y="accidents",
        title=f"Top Hotspots in {selected_city}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )