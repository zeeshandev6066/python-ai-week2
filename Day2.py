# Today’s Goal

# By the end of today, you will:

# Load real datasets from CSV files
# Inspect and understand client data
# Avoid common beginner mistakes


# Step 1: Create a CSV File

# Create products.csv:

# product,price,quantity
# Laptop,80000,5
# Mouse,1500,20
# Keyboard,3000,10


# Step 2: Read CSV with Pandas

import pandas as pd

df=pd.read_csv("/home/bahl/Zeeshan/Learn/AI/my_scripts/Week 2/DAY 2: Reading CSV Files/products.csv")
print(df)


# df = pd.read_csv("products.csv")
# print(df)

# Step 3: Inspect Data

print(df.head())
print(df.info())
print(df.describe())


# Practice Tasks (Must Do)
# Task 1: Print Columns

print(df.columns)

# Task 2: Select One Column
print(df["product"])


# Task 3: Calculate Total Stock Value

# price × quantity for each product

df["total_value"]=df["price"]*df["quantity"]
print(df)


