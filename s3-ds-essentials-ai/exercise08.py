import pandas as pd

# Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

# Pandas
data = {"Name" : ["Alice", "Bob"], "Age" : [25, 30]}
df = pd.DataFrame(data)
print(df)

# Read data from excel or csv
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# to save data frame in excel or csv
df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)

# Viewing Data
print(df.head())
print(df.tail(3))

print(df.info())
print(df.describe())


# selecting and indexing
print(df["Names", "Age"])
print(df[df["Age"] > 25])

print(df.iloc[0])
print(df.iloc[:, 0])

print(df.loc[0])
print(df.loc[:, "Name"])
