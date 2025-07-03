import numpy as np
from scipy.stats import norm

# Generate random sample data
data = np.random.normal(loc=50, scale=10, size=100)
print(data)

# Sample statistics
mean = np.mean(data)
print("Mean: ", mean)

std = np.std(data, ddof=1)
print("Standard Deviation: ", std)

n = len(data)

#95% confidence interval
z_value = norm.ppf(0.975)
margin_of_error = z_value * (std/np.sqrt(n))
ci = (mean - margin_of_error, mean + margin_of_error)

print("95% Confidence Interval: ", ci)
