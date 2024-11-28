#  16. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
#  contains information about the passengers who boarded the unfortunate
#  Titanic ship. Write a code to check how the price of the ticket (column
#  name: 'fare') for each passenger is distributed by plotting a histogram.

import seaborn as sns
import matplotlib.pyplot as plt

# Load the inbuilt Titanic dataset from seaborn
df = sns.load_dataset('titanic')

# Check if 'fare' column exists
if 'fare' in df.columns:
    # Plot the histogram of 'fare'
    plt.figure(figsize=(10, 6))
    plt.hist(df['fare'].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Ticket Fare on Titanic', fontsize=16)
    plt.xlabel('Fare', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', alpha=0.75)
    plt.show()
else:
    print("'fare' column not found in the dataset.")
    