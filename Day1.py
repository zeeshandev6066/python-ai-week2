# Today’s Goal

# Learn how to load and explore data using Pandas.

# Step 1: Install Pandas

# In terminal:
# pip install pandas


# Step 2: Pandas Basics

import pandas as pd

data={
    "name":["Talha","Umer","Imran"],
    "age":["22","25","28"],
    "score":["90","85","75"]
}

df=pd.DataFrame(data)
print(df)

# Step 3: Basic Data Exploration

print(df.head())
print(df.info())
print(df.describe())


# Practice Tasks (Must Do)

# Task 1: Create DataFrame

# Create a DataFrame with:
# product name
# price
# quantity


data={
    "ProductName":["Shampoo","Soap","HairOil"],
    "Price":[500,150,250],
    "Quantity":[3,10,5]
}

df=pd.DataFrame(data)
print(df)


# Task 2: Access Column
# Print only one column (e.g., Price)

df=pd.DataFrame(data)
print(df["Price"])
print(df["Price"].tolist())


# Task 3: Calculate Average

# Find average of a numeric column

average_price = df["Price"].mean()
print("Average price:", average_price)

