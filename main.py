from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_transformation import transform_data
from src.analysis import do_analysis
from src.visualization import make_graphs
from src.report import make_report


print("======================================")
print("SOCIAL MEDIA ENGAGEMENT ANALYSIS")
print("======================================")


print("\nLoading data...")
df = load_data()

print("Number of rows and columns:", df.shape)

print("\nFirst 5 records:")
print(df.head())


print("\nCleaning data...")
df = clean_data(df)


print("\nDoing data transformation...")
df = transform_data(df)


print("\nDoing analysis...")
do_analysis(df)


print("\nCreating graphs...")
make_graphs(df)


print("\nCreating PDF report...")
make_report(df)


print("\nProject completed successfully!")
