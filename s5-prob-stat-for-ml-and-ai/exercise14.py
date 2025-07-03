# Perform a Chi-Square Test
from scipy.stats import chi2_contingency, f_oneway

# Contigency Table
data = [[50, 30, 20], [30, 40, 30]]

# Perform Chi_Square Test
chi2, p, dof, expected = chi2_contingency(data)
print("Chi-Square Statistic: ", chi2)
print("P-Value: ", p)
print("Expected Frequencies: \n", expected)
print("DOF : ", dof)


# F ONEWAY

# Data for groups
group1 = [10,12,14,16,18]
group2 = [9,11,13,15,17]
group3 = [8,10,12,14,16]

# Perform ANOVA
f_stat, p_value = f_oneway(group1, group2, group3)
print("F-Statistic: ", f_stat)
print("P-Value: ", p_value)
