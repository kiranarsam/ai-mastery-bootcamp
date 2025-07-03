# import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

# Discrete random variable: Dice roll
outcomes = [1,2,3,4,5,6]
probabilities = [1/6] * 6

print("Outcomes = ", outcomes)
print("Probability = ", probabilities)

# plt.bar(outcomes, probabilities, color="blue", alpha=0.7)
# plt.title("PMF of a Dice Roll")
# plt.xlabel("Outcomes")
# plt.ylabel("Probability")
# plt.show()


# Continuous random variable: Uniform Distribution

x = np.linspace(0, 1, 10)
pdf = uniform.pdf(x, loc=0, scale=1)
print("x = ", x)
print("pdf = ", pdf)
# plt.plot(x, pdf, color="red")
# plt.title("PDF of Uniform(0,1)")
# plt.xlabel("x")
# plt.ylable("f(x)")
# plt.show()
