#  12.Use Iris flower dataset and perform following :
#  1. Create a box plot for each feature in the dataset.
#  2. Identify and discuss distributions and identify outliers from them

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

file_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\IRIS.csv'
data = pd.read_csv(file_path)

print(data.head(6))

numeric_feature = data.columns[:-1]

for feature in numeric_feature:
    plt.figure(figsize=(8,4))
    sns.boxplot(x=data[feature])
    plt.title(f"the box plot of {feature}")
    plt.xlabel(feature)
    plt.show()

print("\n Outlier Analysis \n")

for feature in numeric_feature:

    q1 = data[feature].quantile(0.25)   #1st quantile
    q3 = data[feature].quantile(0.75)   #3rd quantile
    iqr = q3 - q1    # Interquartile range (IQR)
    lower_bound =q1 - 1.5*iqr  # Lower bound for outliers
    upper_bound = q3 + 1.5 * iqr      # Upper bound for outliers

    outliers = data[(data[feature] < lower_bound) | (data[feature] > upper_bound)]
    print(f"- {feature}: {len(outliers)} outliers") 


input()