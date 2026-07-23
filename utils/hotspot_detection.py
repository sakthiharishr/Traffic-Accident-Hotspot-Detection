def detect_hotspots(df):

    df = df.copy()

    df["lat_bin"] = df["latitude"].round(2)
    df["lon_bin"] = df["longitude"].round(2)

    df["cluster"] = (
        df["lat_bin"].astype(str)
        + "_"
        + df["lon_bin"].astype(str)
    )

    return df