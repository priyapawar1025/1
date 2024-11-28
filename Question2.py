# 2. Perform the following operations using Python on the Telecom_Churn
#  dataset. Compute and display summary statistics for each feature available
#  in the dataset using separate commands for each statistic. (e.g. minimum
#  value, maximum value, mean, range, standard deviation, variance and
#  percentiles)
import pandas as pd
import numpy as np

# Load the dataset
# Replace 'Telecom_Churn.csv' with the actual path to your dataset
dataset_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\Telecom Churn.csv'
df = pd.read_csv(dataset_path)

# Summary statistics
for column in df.select_dtypes(include=np.number).columns:
    print(f"Statistics for column:{[column]}")
    print(f"minimum value:{df[column].min()}")
    print(f"maximum value:{df[column].max()}")
    print(f"mean:{df[column].mean()}")
    print(f"standard deviation:{df[column].std()}")
    print(f"Variance: {df[column].var()}")
    print(f"percentiles(25,50,75):{np.percentile(df[column].dropna(),[25,50,75])}")
    print("-" * 50)

input()
# import pandas as pd
# import numpy as np

# # Load the dataset
# # Replace 'Telecom_Churn.csv' with the actual path to your dataset
# dataset_path = 'Telecom_Churn.csv'
# df = pd.read_csv(dataset_path)

# for column in df.select_dtypes(include=[np.number]).columns:  # Process numerical columns only
#     print(f"Statistics for column: {column}")
#     print(f"Minimum Value: {df[column].min()}")
#     print(f"Maximum Value: {df[column].max()}")
#     print(f"Mean: {df[column].mean()}")
#     print(f"Range: {df[column].max() - df[column].min()}")
#     print(f"Standard Deviation: {df[column].std()}")
#     print(f"Variance: {df[column].var()}")
#     print(f"Percentiles (25th, 50th, 75th): {np.percentile(df[column].dropna(), [25, 50, 75])}")
#     print("-" * 50)
