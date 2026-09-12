import os
import matplotlib.pyplot as plt
import seaborn as sns
from .config import graph_path

def make_graphs(df):

    # 1. Likes Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["Likes"], bins=30)
    plt.title("Likes Distribution")
    plt.xlabel("Likes")
    plt.ylabel("Number of Posts")
    plt.savefig(os.path.join(graph_path, "1_likes_histogram.png"))
    plt.close()

    # 2. Comments Histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["Comments"], bins=30)
    plt.title("Comments Distribution")
    plt.xlabel("Comments")
    plt.ylabel("Number of Posts")
    plt.savefig(os.path.join(graph_path, "2_comments_histogram.png"))
    plt.close()

    # 3. Platform Bar Chart
    platform = df.groupby("Platform")["Total_Engagement"].mean()

    plt.figure(figsize=(8, 5))
    platform.plot(kind="bar")
    plt.title("Average Engagement by Platform")
    plt.xlabel("Platform")
    plt.ylabel("Average Engagement")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(graph_path, "3_platform_bar.png"))
    plt.close()

    # 4. Engagement Pie Chart
    engagement = df.groupby("Platform")["Total_Engagement"].sum()

    plt.figure(figsize=(7, 7))
    plt.pie(
        engagement,
        labels=engagement.index,
        autopct="%1.1f%%"
    )
    plt.title("Engagement by Platform")
    plt.savefig(os.path.join(graph_path, "4_engagement_pie.png"))
    plt.close()

    # 5. Monthly Posting Trend
    monthly = df.groupby("Month").size()

    plt.figure(figsize=(10, 5))
    monthly.plot(marker="o")
    plt.title("Monthly Posting Trend")
    plt.xlabel("Month")
    plt.ylabel("Number of Posts")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(graph_path, "5_monthly_trend.png"))
    plt.close()

    # 6. Views Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["Views"], bins=30)
    plt.title("Views Distribution")
    plt.xlabel("Views")
    plt.ylabel("Number of Posts")
    plt.savefig(os.path.join(graph_path, "6_views_histogram.png"))
    plt.close()

    # 7. Views vs Engagement
    plt.figure(figsize=(8, 5))
    plt.scatter(
        df["Views"],
        df["Total_Engagement"],
        alpha=0.5
    )
    plt.title("Views vs Total Engagement")
    plt.xlabel("Views")
    plt.ylabel("Total Engagement")
    plt.savefig(os.path.join(graph_path, "7_views_engagement.png"))
    plt.close()

    # 8. Likes Box Plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df["Likes"])
    plt.title("Likes Box Plot")
    plt.xlabel("Likes")
    plt.savefig(os.path.join(graph_path, "8_likes_boxplot.png"))
    plt.close()

    # 9. Correlation Heatmap
    columns = [
        "Likes",
        "Comments",
        "Shares",
        "Views",
        "Saves",
        "Follower_Count",
        "Engagement_Rate",
        "Hashtag_Count",
        "Content_Length"
    ]

    plt.figure(figsize=(10, 7))
    sns.heatmap(
        df[columns].corr(),
        annot=True,
        fmt=".2f"
    )
    plt.title("Correlation Heatmap")
    plt.savefig(os.path.join(graph_path, "9_correlation_heatmap.png"))
    plt.close()

    # 10. Pair Plot
    columns = [
        "Likes",
        "Comments",
        "Shares",
        "Views",
        "Saves"
    ]

    sns.pairplot(
        df[columns].sample(
            min(500, len(df)),
            random_state=1
        )
    )

    plt.savefig(
        os.path.join(graph_path, "10_pair_plot.png")
    )

    plt.close("all")
