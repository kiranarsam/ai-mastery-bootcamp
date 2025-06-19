# grouping data

grouped = df.groupby("column_name")

# iterate
for name, group in grouped:
  print(name)
  print(group)

grouped.mean()
grouped.sum()

df.groupby("category_column")["numeric_column"].mean()
# Using aggregation
df.groupby("category_column").agg({"numeric_column" : ["mean", "max", "min"]})
# using pivot table
pivot = df.pivot_table(
  values="numeric_column",
  index="category_column",
  aggfunc="mean"
)

# custom aggregation func
def range_func(x):
  return x.max() - x.min()

df.groupby("category_column")["numeric_column"].agg(range_func)


# calculating summary statistics data
df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column")["numeric_column"].max()
df.groupby("category_column")["numeric_column"].min()

df.groupby("category_column").agg(
  {"numeric_column" : ["mean", "max", "min"]}
)
