import pandas as pd
import numpy as np

file_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\Covid Vaccine Statewise.csv'
df= pd.read_csv(file_path)

print(df.head())

data_description = df.describe()
print("data description:",data_description)

#Number of Males vaccinated
males_vaccinated = df.groupby('State')['Male (Doses Administered)'].sum()
print("\n Number of Males vaccinated \n",males_vaccinated)

#Number of females vaccinated

females_vaccinated = df.groupby('State')['Male (Doses Administered)'].sum()
print("\n Number of females vaccinated \n",females_vaccinated)
input()