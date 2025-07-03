#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load DataSet
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df = pd.read_csv(url)

# Analyse sepal_length
feature = df["sepal_length"]
print("Skewness: ", skew(feature))
print("Kurtosis: ", kurtosis(feature))

# visualise distribution
sns.heatplot(feature, kde=True)
plt.title("Distribution of Sepal Length")
plt.show()
