#1. Perform the following operations using Python on a data set : read data
#  from different formats(like csv, xls),indexing and selecting data, sort data,
#  describe attributes of data, checking data types of each column. (Use
#  Titanic Dataset)

import pandas as pd

# Load the Titanic dataset
file_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\Titanic.csv'
data = pd.read_csv(file_path)

# 1. Indexing and Selecting Data
selected_data = data.loc[:7,['Name','Age']]
print("Selected Data:\n",selected_data)

#sorting of data
sorted_data = data.sort_values(by ="Name",ascending=True)
print("Sorted data\n",sorted_data)

#descriptive analysis
data_description = data.describe()
print("descriptive_values\n",data_description)

#data types
data_types = data.dtypes
print("data types\n",data_types)


input()

