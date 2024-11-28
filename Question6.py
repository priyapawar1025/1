#  6. Write a program to do: A dataset collected in a cosmetics shop showing
#  details of customers and whether or not they responded to a special offer
#  to buy a newlip-stick is shown in table below. (Use library commands)
#  According to the decision tree you have made from the previous training
#  data set, what is the decision for the test data: [Age > 35, Income =
#  Medium, Gender = Female, Marital Status = Married]?
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
file_path = r"C:\Users\pawar\OneDrive\Desktop\DSML Practical\Lipstick.csv" # Use the uploaded file path
df = pd.read_csv(file_path)

# Display the dataset
print("Dataset:")
print(df.head())

# Encode categorical features into numerical values
df['Age'] = df['Age'].map({'<21': 0, '21-35': 1, '>35': 2})  # Encoding for Age
df['Income']= df['Income'].map({'Low':0,'Medium':1,'High':2})
df['Gender']=df['Gender'].map({'Male': 0, 'Female': 1})
df['Ms']= df['Ms'].map({'Single': 0, 'Married': 1})
df['Buys']=df['Buys'].map({'No': 0, 'Yes': 1})

# Features (input columns) and target (output column)
x =df[['Age','Income','Gender','Ms']]
y =df['Buys']

# Train the decision tree model
clf = DecisionTreeClassifier()
clf.fit(x,y)

# Define the test data: [Age > 35, Income = Medium, Gender = Female, Marital Status = Married]

test_data=pd.DataFrame([[2,1,1,1]], columns=['Age', 'Income', 'Gender', 'Ms'])

# Make a prediction using the trained model
prediction = clf.predict(test_data)

# Display the result
if prediction[0] == 1:
    print("\nPrediction: The customer will buy the lipstick (Yes).")
else:
    print("\nPrediction: The customer will not buy the lipstick (No).")


