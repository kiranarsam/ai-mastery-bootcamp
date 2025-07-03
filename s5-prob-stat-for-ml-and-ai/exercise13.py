# Conduct T-Tests
# Perform one-sample, two-sample and paired t-tests
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel

# one-Sample T-Test
data = [12,14,15,16,17]
pupulation_mean = 15
t_stat, p_value = ttest_1samp(data, pupulation_mean)
print("One-Sample T-Test: ", t_stat, p_value)

# Two-Sample T-Test
group1 = [12,14,15,16,17]
group2 = [11, 13, 14, 15, 16]
t_stat, p_value = ttest_ind(group1, group2)
print("Two-Sample T-Test: ", t_stat, p_value)

#Paired -Sample T-Test
pre_test = [12, 14, 15, 16, 17]
post_test = [13, 14, 16, 17, 18]
t_stat, p_value = ttest_rel(pre_test, post_test)
print("Paired T-Test: ", t_stat, p_value)
