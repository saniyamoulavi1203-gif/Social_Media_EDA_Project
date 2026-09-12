import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_file = os.path.join(
    base_path, "data", "raw data", "social_media_engagement_dataset.csv"
)

cleaned_file = os.path.join(
    base_path, "data", "processed", "social_media_cleaned.csv"
)

graph_path = os.path.join(base_path, "outputs", "graphs")
analysis_path = os.path.join(base_path, "outputs", "analysis")
report_path = os.path.join(base_path, "outputs", "reports")

os.makedirs(graph_path, exist_ok=True)
os.makedirs(analysis_path, exist_ok=True)
os.makedirs(report_path, exist_ok=True)
