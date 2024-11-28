#  24. Perform the following operations using Python on a suitable data set,
#  counting unique values of data, format of each column, converting variable
#  data type (e.g. from long to short, vice versa), identifying missing values
#  and filling in the missing values.

import pandas as pd 

file_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\Lipstick.csv'
df = pd.read_csv(file_path)

#counting unique values and data types 

print("\n unique values:\n ",df.nunique())
print("\n data types:",df.dtypes)

# converting variable data type (e.g. from long to short, vice versa)

df.update(df.select_dtypes('float64').apply(lambda x : x.astype('int64')if (x % 1).eq(0).all() else x))
df.update(df.select_dtypes('int64').astype('str'))

# Handle missing values: Fill numerical with mean, categorical with mode
df.fillna({col: df[col].mean() for col in df.select_dtypes(['float64', 'int64'])}, inplace=True)
df.fillna({col: df[col].mode()[0] for col in df.select_dtypes(['object'])}, inplace=True)

# Save cleaned data
df.to_csv(r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\Lipstick.csv', index=False)
print("\nCleaned data saved successfully!")




