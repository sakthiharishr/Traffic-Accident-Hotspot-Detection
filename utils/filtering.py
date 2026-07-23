def apply_filters(
    df,
    states,
    cities,
    weather,
    severity
):

    if states:
        df = df[df["state"].isin(states)]

    if cities:
        df = df[df["city"].isin(cities)]

    if weather:
        df = df[df["weather"].isin(weather)]

    if severity:
        df = df[df["accident_severity"].isin(severity)]

    return df