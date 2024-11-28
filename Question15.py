# 15. Use the dataset 'titanic'. The dataset contains 891 rows and contains
#  information about the passengers who boarded the unfortunate Titanic
#  ship. Use the Seaborn library to see if we can find any patterns in the data

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

file_path =r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\Titanic.csv'
df = pd.read_csv(file_path)
print(df.head())

print(df.info())


print(df.isnull().sum())

#Survival rate by gender
sns.countplot(x='Survived',hue='Sex',data=df)
plt.title("Survival rate of gender")
plt.ylabel('count')
plt.xlabel('Survived(0=No,1=Yes)')
plt.show()

#Survival rate by Passenger class
sns.countplot(x='Survived',hue='Pclass',data=df)
plt.title("Survival rate by passanger")
plt.xlabel('Survived(0 = No, 1= Yes)')
plt.ylabel('count')
plt.show()

#Age Distribution of Passengers
sns.histplot(df['Age'],kde='True',bins=20)
plt.title("Distribution of passangers")
plt.xlabel('Age')
plt.ylabel('frequency')
plt.show()

#Distribution of Ticket Fare on Titanic
plt.figure(figsize=(10, 6))
plt.hist(df['Fare'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Ticket Fare on Titanic', fontsize=16)
plt.xlabel('Fare', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', alpha=0.75)
plt.show()

#corelation of fare and survival
sns.boxplot(x='Survived',y='Fare',data=df)
plt.title("corelation of fare and survival")
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Fare')
plt.show()

input()