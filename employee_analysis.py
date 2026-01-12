# Today’s Goal

# Build a complete data workflow like a real client task:
# Load data → Clean → Analyze → Visualize
# This is portfolio-ready

# MINI PROJECT: Employee Data Analysis
# Input File: employee_data.csv

# name,age,salary
# Ali,25,50000
# Sara,,60000
# Ahmed,30,
# Ayesha,28,55000

import pandas as pa
import matplotlib.pyplot as plt

#Load Data

df=pa.read_csv("/home/bahl/Zeeshan/Learn/AI/my_scripts/Week 2/DAY 6: Mini Data Project (Freelance-Style)/employee_data.csv")

#Clean Data

df["age"].fillna(df["age"].mean(),inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)

#Analyze Data

print("Average Salary",df["salary"].mean())
print("Average age",df["age"].mean())
print("Total Number of Employee",df.shape[0])

#Visualize Data

plt.bar(df["name"],df["salary"])
plt.title("Salary By Employee")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()


