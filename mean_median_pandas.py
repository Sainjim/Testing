import pandas as pd
import numpy as np

# Load the CSV file

data = pd.read_csv("mean.csv")

# Calculate mean and median
mean_value = np.mean(data)
median_value = np.median(data)

# Display the results
print("Mean:", mean_value)
print("Median:", median_value)