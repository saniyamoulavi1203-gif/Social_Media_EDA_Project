def transform_data(df):
    df = df.copy()

    # Total engagement of every post
    df["Total_Engagement"] = (
        df["Likes"]
        + df["Comments"]
        + df["Shares"]
        + df["Saves"]
    )

    # Get month from timestamp
    df["Month"] = df["Timestamp"].dt.to_period("M").astype(str)

    # Get date
    df["Date"] = df["Timestamp"].dt.date

    return df
