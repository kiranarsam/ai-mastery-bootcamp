import numpy as np
import matplotlib.pyploy as plt
from scipy.stats import norm, binom, uniform, poisson
import seaborn as sns

# Gaussian Distribution
x = np.linspace(-4, 4, 100)
print("x = ", x)
plt.plot(x, norm.pdf(x, loc=0, scale=1), label="Gaussian (u=0, s=1)")

# binomial Distribution
n, p = 10, 0.5
x = np.arange(0, n+1)
plt.bar(x, binom.pmf(x, n, p), alpha=0.7, label="Binomial (n=10, p=0.5)")

# Poisson Distribution
lam = 3
x = np.arange(0, 10)
plt.bar(x, poisson.pmf(x, lam), alpha=0.7, label="Poisson (l=3)")

# uniform distribution
x = np.random.uniform(low=0, high=10, size=1000)
sns.histplot(x, kde=True, label="Uniform", color="red")

plt.title("Probability Distributions")
plt.legend()
plt.show()
