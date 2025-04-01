import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load and Explore the Dataset
file_path =  "C:/Users/MUIKO/Downloads/Electric_Vehicle_Population_Data.csv"
try:
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Display the first few rows
    print("First few rows of the dataset:")
    print(df.head())
    
    # Check data types and missing values
    print("\nDataset Info:")
    df.info()
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Handle missing values
    df.fillna({'County': 'Unknown', 'City': 'Unknown', 'Postal Code': df['Postal Code'].mode()[0],
               'Electric Range': df['Electric Range'].median(), 'Base MSRP': df['Base MSRP'].median(),
               'Legislative District': df['Legislative District'].mode()[0],
               'Vehicle Location': 'Unknown', 'Electric Utility': 'Unknown'}, inplace=True)
    
except FileNotFoundError:
    print("Error: The dataset file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping by Electric Vehicle Type and computing mean Electric Range
print("\nMean Electric Range by Vehicle Type:")
print(df.groupby('Electric Vehicle Type')['Electric Range'].mean())

# Data Visualization
sns.set(style="whitegrid")

# Line Chart: Number of electric vehicles by Model Year
plt.figure(figsize=(10,5))
df['Model Year'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title("Electric Vehicles Registered per Model Year")
plt.xlabel("Model Year")
plt.ylabel("Number of Vehicles")
plt.show()

# Bar Chart: Average Electric Range by Make
plt.figure(figsize=(12,6))
sns.barplot(x=df['Make'], y=df['Electric Range'], estimator=np.mean, ci=None)
plt.xticks(rotation=90)
plt.title("Average Electric Range by Car Make")
plt.xlabel("Car Make")
plt.ylabel("Average Electric Range")
plt.show()

# Histogram of Electric Range
plt.figure(figsize=(10,5))
plt.hist(df['Electric Range'], bins=20, edgecolor='black')
plt.title("Distribution of Electric Range")
plt.xlabel("Electric Range (miles)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Base MSRP vs. Electric Range
plt.figure(figsize=(10,5))
sns.scatterplot(x='Base MSRP', y='Electric Range', data=df)
plt.title("Scatter Plot of Base MSRP vs. Electric Range")
plt.xlabel("Base MSRP ($)")
plt.ylabel("Electric Range (miles)")
plt.show()

# Findings and Observations
print("\nFindings and Observations:")
print("1. The dataset contains electric vehicle registration data, including make, model, and electric range.")
print("2. Missing values in critical columns were filled using median or mode values.")
print("3. Most vehicles belong to a few major manufacturers, with varying electric ranges.")
print("4. Visualization reveals trends in electric vehicle adoption over the years.")
