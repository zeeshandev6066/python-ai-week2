# Today’s Goal

# Learn how to:

# Handle missing values
# Fix wrong data types
# Prepare data for AI/ML
# This is one of the highest-paid freelance skills.

# Create dirty_data.csv:

# name,age,salary
# Ali,25,50000
# Sara,,60000
# Ahmed,30,
# Ayesha,28,55000


# Step 2: Load Data

import pandas as pd

df=pd.read_csv("/home/bahl/Zeeshan/Learn/AI/my_scripts/Week 2/DAY 3: Data Cleaning/dirty_data.csv")
print(df)


# Step 3: Detect Missing Values

print(df.isnull())
print(df.isnull().sum())


# Step 4: Handle Missing Values
# Option 1: Fill Missing


df["age"].fillna(df["age"].mean(),inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)
print(df)

# Option 2: Drop Rows

df.dropna(inplace=True)
print(df)


# Practice Tasks (Must Do)

# Task 1:
# Fill missing age with average age.

# Task 2:
# Fill missing salary with average salary.

# Task 3:
# Print cleaned DataFrame.