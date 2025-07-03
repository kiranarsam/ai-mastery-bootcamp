import numpy as np

# Random variables: dice roll
outcomes = np.array([1,2,3,4,5,6])
print("Outcomes: ", outcomes)
probabilities = np.array([1/6]*6)
print("Probabilities: ", probabilities)


# Expectation
expectation = np.sum(outcomes * probabilities)
print("Expectations: ", expectation)

# Variance and Standard Deviation
variance = np.sum((outcomes - expectation)**2 * probabilities)

std_dev = np.sqrt(variance)
print("Variance = ", variance)
print("Standard Deviation = ", std_dev)
