import numpy as np
from scipy.stats import norm, t

# Sample data
data = [12, 14, 15, 16, 17, 18, 19]

# Calculate meand and standard deviation
mean = np.mean(data)
std_dev = np.std(data, ddof=1)

# 95% Confidence Interval (Using t-distribution)
n = len(data)
t_value = t.ppf(0.975, df=n-1)
margin_of_error = t_value * (std_dev / np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)

print("95% Confidence Interval: ", ci)
