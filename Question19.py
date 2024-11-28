import pandas as pd 

file_path = r'C:\Users\pawar\OneDrive\Desktop\DSML Practical\IRIS.csv'
data = pd.read_csv(file_path)

print(data.head())


# Filter the dataset for each species
species_list= ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Iterate through each species and display statistical details
for species in species_list:
    print(f"statistics for {species}:")
    species_data = data[data['species']== species]     # Filter data for the species
    data_description = species_data.describe() # Display statistical details
    print(data_description)
    print("\n")


