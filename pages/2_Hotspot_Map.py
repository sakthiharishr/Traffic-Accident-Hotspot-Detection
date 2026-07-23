import streamlit as st
import pydeck as pdk

from utils.data_loader import load_data
from utils.hotspot_detection import detect_hotspots
from utils.hotspot_ranking import get_top_hotspots

st.title("🗺️ Accident Hotspot Map")

df = load_data()

selected_city = st.selectbox(
    "Select City",
    sorted(df["city"].unique())
)

city_df = df[
    df["city"] == selected_city
]

city_df = detect_hotspots(city_df)

hotspots = get_top_hotspots(city_df)

if len(hotspots) == 0:

    st.warning(
        "No hotspots detected."
    )

else:

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=hotspots,
        get_position='[longitude, latitude]',
        get_fill_color='[255,0,0,180]',
        get_radius=800,
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=city_df["latitude"].mean(),
        longitude=city_df["longitude"].mean(),
        zoom=10
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={
            "html": """
            <b>Hotspot:</b> {hotspot_id}<br/>
            <b>Accidents:</b> {accidents}<br/>
            <b>Average Risk:</b> {avg_risk}
            """
        }
    )

    st.pydeck_chart(deck)