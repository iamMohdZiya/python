# write a program to clean the data using numpy or pandas libraries
import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Alice"],
    "Age": [25, np.nan, 30, 29, 25],
    "Salary": [50000, 60000, np.nan, 58000, 50000],
    "Joining_Date": ["2021-05-20", "2021-06-15", "NaN", "2021-08-01", "2021-05-20"],
    "Gender": ["F", "M", np.nan, "M", "F"]
}

df = pd.DataFrame(data)
print("Original Data:", df)


df['Age'] = df['Age'].fillna(df['Age'].mean())          
df['Salary'] = df['Salary'].fillna(df['Salary'].median()) 
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0]) 
df['Joining_Date'] = df['Joining_Date'].replace("NaN", np.nan).fillna("Unknown")


df = df.drop_duplicates()
print(end="")
print("cleaned data:")
print(df)


