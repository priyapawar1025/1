import pandas as pd 
import numpy as np

file_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\Covid Vaccine Statewise.csv'
df = pd.read_csv(file_path)

print (df.head(5))

data_types = df.dtypes
print(data_types)

data_description = df.describe()
print("Description of data:",data_description)

# b. Number of persons state wise vaccinated for first dose in India
first_dose_vaccinated = df.groupby('State')['First Dose Administered'].sum()
print("\nNumber of persons state-wise vaccinated for first dose:")
print(first_dose_vaccinated)

#Number of persons state wise vaccinated for second dose in India
sec_dose_vaccinated = df.groupby('State')['Second Dose Administered'].sum()
print("\nNumber of persons state-wise vaccinated for second dose:")
print(sec_dose_vaccinated)


input()