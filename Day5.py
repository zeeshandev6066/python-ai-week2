# Today’s Goal

# Learn how to:

# Visualize data
# Explain insights visually
# Add professional value to your freelance work

# Step 1: Install Libraries

# pip install matplotlib


# Step 2: Basic Plot (Salary)

import pandas as pa
import matplotlib.pyplot as plt

df=pa.read_csv("/home/bahl/Zeeshan/Learn/AI/my_scripts/Week 2/DAY 5: Data Visualization (Insights That Sell)/dirty_data.csv")
df["age"].fillna(df["age"].mean(),inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)

plt.plot(df["salary"])
plt.title("Salary Distribution")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()


# Step 3: Bar Chart (Names vs Salary)

plt.bar(df["name"],df["salary"])
plt.title("Salary by Employee")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()

# Practice Tasks (Must Do)
# Task 1:
# Create a bar chart of age vs name.

plt.bar(df["name"],df["age"])
plt.title("Age by Name")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()


# Task 2:
# Create a line chart of salary.

plt.plot(df["salary"])
plt.title("Salary Chart")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()

