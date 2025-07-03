from scipy.stats import chi2_contingency, f_oneway

# Contingency Table
data = [[50, 30], [20, 40]]

#Perform Chi-Sqaure Test
chi2, p, dof, expected = chi2_contingency(data)
print("Chi-Square Statistic: ", chi2)
print("P-Value: ", p)
print("Expected Frequencies: \n", expected)
print("DOF : ", dof)

# Data for three groups
group1 = [12,13,15,16,17]
group2 = [12,13,18,16,17]
group3 = [10,13,15,16,17]

# perform ANOVA
f_stat, p_value = f_oneway(group1, group2, group2)
print("F-Statistic: ", f_stat)
print("P-Value: ", p_value)
