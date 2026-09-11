import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from .config import report_path, graph_path

def make_report(df):

    file_name = os.path.join(
        report_path,
        "Social_Media_EDA_Report.pdf"
    )

    document = SimpleDocTemplate(
        file_name,
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph(
            "Social Media Engagement Analysis",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    

    

    story.append(
        Paragraph(
            "Total Posts: " + str(len(df)),
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Average Likes: "
            + str(round(df["Likes"].mean(), 2)),
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Average Comments: "
            + str(round(df["Comments"].mean(), 2)),
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Total Engagement: "
            + str(df["Total_Engagement"].sum()),
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Business Insights",
            styles["Heading2"]
        )
    )

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

    story.append(
        Paragraph(
            "Best Platform: " + str(best_platform),
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Best Content Type: " + str(best_content),
            styles["Normal"]
        )
    )

    # Add the graphs to the report
    graph_names = [
        "1_likes_histogram.png",
        "2_comments_histogram.png",
        "3_platform_bar.png",
        "4_engagement_pie.png",
        "5_monthly_trend.png",
        "6_views_histogram.png",
        "7_views_engagement.png",
        "8_likes_boxplot.png",
        "9_correlation_heatmap.png",
        "10_pair_plot.png"
    ]

    for graph in graph_names:

        path = os.path.join(
            graph_path,
            graph
        )

        if os.path.exists(path):
            story.append(Spacer(1, 15))
            story.append(
                Image(
                    path,
                    width=450,
                    height=280
                )
            )

    document.build(story)
