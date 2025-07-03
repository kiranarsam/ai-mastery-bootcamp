from scipy.stats import ttest_ind

# Define from two groups
group1 = [11, 12, 13, 14, 15, 16, 17]
group2 = [13, 14, 15, 16, 17, 18, 19]

# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)
print("T Statistic: ", t_stat)
print("P Value: ", p_value)

alpha = 0.05

if p_value <= alpha:
  print("Reject the NULL hypothesis: significant difference")
else:
  print("Fail to reject the NULL hypothesis: no significant difference")
