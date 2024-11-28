# 11. Use Iris flower dataset and perform following :
#  1. List down the features and their types (e.g., numeric, nominal)
#  available in the dataset. 2. Create a histogram for each feature in the
#  dataset to illustrate the feature distributions.
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\IRIS.csv'
df = pd.read_csv(file_path)

print(df.head(5))
# 1. List down the features and their types (e.g., numeric, nominal) available in the dataset.
feature_types = df.dtypes
print(feature_types)
print ("-"*50)

print("features and their types:")
for column in df.columns:
    if(df[column].dtype) == 'float64':
        print(f"- {column} -> (Numeric)")
    else:
        print(f"- {column} -> (Nominal)")

# numeric_features =df.columns[:-1]

# for feature in numeric_features:
#     sns.histplot(df[feature], kde=True, bins=20)
#     plt.title(f"Histogram of {feature}")
#     plt.xlabel(feature)
#     plt.ylabel("Frequency")
#     plt.show()

numeric_feature = df.columns[:-1]

for feature in numeric_feature:
    plt.figure(figsize=(10,9))
    sns.histplot(df[feature],kde=True,bins=10) #kde = kernel density estimate
    plt.title(f"the histogram of{feature}")
    plt.xlabel(feature)
    plt.ylabel("frequency")
    plt.show()


input()