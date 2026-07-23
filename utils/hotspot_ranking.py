def get_top_hotspots(df):

    hotspots = (
        df.groupby("cluster")
        .agg(
            latitude=("latitude","mean"),
            longitude=("longitude","mean"),
            accidents=("cluster","size"),
            avg_risk=("risk_score","mean")
        )
        .reset_index()
    )

    hotspots = hotspots.sort_values(
        "accidents",
        ascending=False
    )

    return hotspots.head(10)