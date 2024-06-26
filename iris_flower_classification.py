# -*- coding: utf-8 -*-
"""IRIS FLOWER CLASSIFICATION.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pqqcr54HrulgdkKwVDJxSUH3qrdz_cn4

Load the dataset
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
iris_data = pd.read_csv("IRIS Flower.csv")

"""Explore the dataset"""

# Print the first few rows
iris_data.head()

# Get basic information about the dataset
iris_data.info()

iris_data.describe()

# Plot using seaborn's pairplot
import seaborn as sns
sns.pairplot(iris_data, hue="species", markers=["o", "s", "D"])
plt.title("Pairplot of Iris Dataset")
plt.show()

"""Preprocess the data"""

# Split the dataset into features (X) and target (y)
X = iris_data.drop('species', axis=1)
y = iris_data['species']
# Display the first few rows of features and target
print("Features (X):")
print(X.head())

print("\nTarget variable (y):")
print(y.head())

# One-hot encode the target variable
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Calculate the average of each feature for all classes
average_features = iris_data.groupby("species").mean()

# Display the average of each feature
print("Average of each feature for all classes:")
print(average_features)

# Calculate the average of each feature for all classes
average_features = iris_data.groupby("species").mean()

# Plot the average of each feature
plt.figure(figsize=(10, 6))
sns.barplot(data=average_features.reset_index(), x="species", y="sepal_length", color="skyblue", label="Sepal Length")
sns.barplot(data=average_features.reset_index(), x="species", y="sepal_width", color="salmon", label="Sepal Width")
sns.barplot(data=average_features.reset_index(), x="species", y="petal_length", color="lightgreen", label="Petal Length")
sns.barplot(data=average_features.reset_index(), x="species", y="petal_width", color="orange", label="Petal Width")
plt.title("Average of each feature for all classes")
plt.xlabel("Species")
plt.ylabel("Average")
plt.legend()
plt.show()

"""Split the data into training and testing sets"""

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)

"""Train a machine learning model"""

from sklearn.ensemble import RandomForestClassifier
# Get the feature names
feature_names = X.columns

# Create a random forest classifier
clf = RandomForestClassifier(warm_start=False, random_state=42)

# Train the model
clf.fit(X_train, y_train)

"""Evaluate the model"""

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Generate a detailed classification report
report = classification_report(y_test, y_pred)

# Print the classification report
print("Classification Report:")
print(report)

"""Make predictions on new data


"""

# Example new data
new_data = [[5.1, 3.5, 5.4, 1.2]]

# Make a prediction
prediction = clf.predict(new_data)
print(f"Predicted species: {encoder.inverse_transform(prediction)[0]}")

