import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
iris = pd.read_csv("C:\\Users\\Sravani Chitrada\\Downloads\\archivs.zip")


print(iris.head())



print(iris.describe())



print("Target Labels", iris["Species"].unique())



import pandas as pd
import plotly.express as px

# Load the Iris dataset
iris_data = pd.read_csv("C:\\Users\\Sravani Chitrada\\Downloads\\archivs.zip")

# Calculate the average sepal length for each species
average_sepal_length = iris_data.groupby('Species')['SepalLengthCm'].mean().reset_index()

# Create a bar graph using Plotly Express
fig = px.bar(average_sepal_length, x='Species', y='SepalLengthCm', color='Species')

# Show the plot
fig.show()
