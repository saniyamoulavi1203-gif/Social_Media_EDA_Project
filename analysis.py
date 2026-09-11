def do_analysis(df):

    print("\n----- BASIC ANALYSIS -----")

    print("Total number of posts:", len(df))

    print(
        "Average likes:",
        round(df["Likes"].mean(), 2)
    )

    print(
        "Average comments:",
        round(df["Comments"].mean(), 2)
    )

    print(
        "Total engagement:",
        df["Total_Engagement"].sum()
    )

    print(
        "Average engagement rate:",
        round(df["Engagement_Rate"].mean(), 2)
    )

    print("\n----- TOP 10 POSTS -----")

    top_posts = df.sort_values(
        "Total_Engagement",
        ascending=False
    ).head(10)

    print(
        top_posts[
            ["Post_ID", "Platform", "Content_Type",
             "Likes", "Comments", "Total_Engagement"]
        ]
    )

    print("\n----- PLATFORM ANALYSIS -----")

    platform = df.groupby("Platform").agg({
        "Post_ID": "count",
        "Likes": "mean",
        "Comments": "mean",
        "Total_Engagement": "mean",
        "Engagement_Rate": "mean"
    })

    platform.columns = [
        "Posts",
        "Average_Likes",
        "Average_Comments",
        "Average_Engagement",
        "Average_Engagement_Rate"
    ]

    print(platform)

    print("\n----- CONTENT TYPE ANALYSIS -----")

    content = df.groupby("Content_Type")["Total_Engagement"].mean()
    print(content.sort_values(ascending=False))

    print("\n----- MONTHLY POSTING TREND -----")

    monthly = df.groupby("Month").size()
    print(monthly)

    print("\n----- SENTIMENT ANALYSIS -----")

    sentiment = df.groupby("Sentiment")["Total_Engagement"].mean()
    print(sentiment.sort_values(ascending=False))

    print("\n----- HIGHEST VIEWS -----")

    highest_views = df.sort_values(
        "Views",
        ascending=False
    ).head(10)

    print(
        highest_views[
            ["Post_ID", "Platform", "Content_Type", "Views"]
        ]
    )

    print("\n----- HASHTAG ANALYSIS -----")

    hashtag = df.groupby("Hashtag_Count")[
        "Total_Engagement"
    ].mean()

    print(hashtag.sort_values(ascending=False))

    # Save a simple business insights file
    best_platform = (
        df.groupby("Platform")["Total_Engagement"]
        .mean()
        .idxmax()
    )

    best_content = (
        df.groupby("Content_Type")["Total_Engagement"]
        .mean()
        .idxmax()
    )

    best_sentiment = (
        df.groupby("Sentiment")["Total_Engagement"]
        .mean()
        .idxmax()
    )

    with open(
        "outputs/analysis/social_media_insights.txt",
        "w"
    ) as file:

        file.write("SOCIAL MEDIA ENGAGEMENT ANALYSIS\n")
        file.write("--------------------------------\n\n")

        file.write(
            "Total Posts: " + str(len(df)) + "\n"
        )

        file.write(
            "Average Likes: "
            + str(round(df["Likes"].mean(), 2))
            + "\n"
        )

        file.write(
            "Average Comments: "
            + str(round(df["Comments"].mean(), 2))
            + "\n"
        )

        file.write(
            "Total Engagement: "
            + str(df["Total_Engagement"].sum())
            + "\n"
        )

        file.write(
            "Best Platform: "
            + str(best_platform)
            + "\n"
        )

        file.write(
            "Best Content Type: "
            + str(best_content)
            + "\n"
        )

        file.write(
            "Best Sentiment: "
            + str(best_sentiment)
            + "\n"
        )

    return platform
