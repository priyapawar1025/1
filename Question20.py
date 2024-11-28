#  20. Write a program to cluster a set of points using K-means for IRIS
#  dataset. Consider, K=3, clusters. Consider Euclidean distance as the
#  distance measure. Randomly initialize a cluster mean as one of the data
#  points. Iterate at least for 10 iterations. After iterations are over, print the
#  final cluster means for each of the clusters

import numpy as np
import pandas as pd
import random

# Load the dataset
file_path = r"C:\Users\pawar\OneDrive\Desktop\DSML Practical\IRIS.csv"
df = pd.read_csv(file_path)

# Extract features (assuming the last column is the target label and we only need features for clustering)
X = df.iloc[:, :-1].values  # First four columns as features

# Number of clusters and iterations
K = 3
iterations = 10

# Step 1: Randomly initialize cluster centers from the data points
np.random.seed(42)
initial_centroids = X[random.sample(range(len(X)), K)]

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Step 2: Implement the K-means algorithm
for iteration in range(iterations):
    # Step 2.1: Assign each point to the nearest centroid
    clusters = {i: [] for i in range(K)}  # Create empty lists for each cluster
    for point in X:
        distances = [euclidean_distance(point, centroid) for centroid in initial_centroids]
        cluster_index = np.argmin(distances)  # Find the nearest centroid
        clusters[cluster_index].append(point)
    
    # Step 2.2: Update centroids to be the mean of the points in each cluster
    new_centroids = []
    for i in range(K):
        new_centroids.append(np.mean(clusters[i], axis=0) if clusters[i] else initial_centroids[i])
    
    # Step 2.3: Check for convergence (if centroids do not change)
    new_centroids = np.array(new_centroids)
    if np.allclose(initial_centroids, new_centroids):
        break
    
    # Update the centroids for the next iteration
    initial_centroids = new_centroids

# Step 3: Output the final cluster means (centroids)
print("Final Cluster Means (Centroids):")
for i, centroid in enumerate(initial_centroids):
    print(f"Cluster {i+1}: {centroid}")
