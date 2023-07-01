import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the dataset
df = pd.read_csv("C:\\Users\\Sravani Chitrada\\Downloads\\archive.zip")


# Step 3: Explore the dataset
df.head()  # Display the first few rows of the DataFrame
df.info()  # Get information about the DataFrame

# Step 4: Prepare the data
df[' Date'] = pd.to_datetime(df[' Date'])

# Step 5: Analyze and visualize the data
plt.figure(figsize=(10, 6))
plt.bar(df[' Date'], df[' Estimated Unemployment Rate (%)'], width=5.6)  # Adjust the width as needed
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)  # Rotate x-axis tick labels for better readability
plt.grid(True)
plt.show()
