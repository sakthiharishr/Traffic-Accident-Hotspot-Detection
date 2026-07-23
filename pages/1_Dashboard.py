import streamlit as st

from utils.data_loader import load_data

st.title("📊 Dashboard")

df = load_data()

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Accidents",
    len(df)
)

col2.metric(
    "Cities",
    df["city"].nunique()
)

col3.metric(
    "Fatal Accidents",
    (df["accident_severity"]=="fatal").sum()
)

col4.metric(
    "Average Risk Score",
    round(df["risk_score"].mean(),2)
)

st.divider()

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)