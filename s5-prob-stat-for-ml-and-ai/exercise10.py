import numpy as np
from scipy.stats import ttest_1samp

# Sample data
data = [12, 14, 15, 16, 17, 18, 19]

# Null Hypothesis: mean = 15
population_mean = 15

# Perform t-test
t_stat, p_value = ttest_1samp(data, population_mean)
print("T-Statistics: ", t_stat)
print("P-Value: ", p_value)

# Interpret results
alpha = 0.5

if p_value <= alpha:
  print("Reject the NULL hypothesis: significant difference")
else:
  print("Fail to reject the NULL hypothesis: no significant difference")
