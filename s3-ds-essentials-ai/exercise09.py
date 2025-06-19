#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# load data set
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore structure
print("First 5 rows: \n", df.head(5))
print("Last 5 rows: \n", df.tail(5))

print(df.info())

print(df.describe())
