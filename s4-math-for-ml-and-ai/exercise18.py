import numpy as np
# import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson

# Gausian Distribution
x = np.linspace(-4, 4, 100)
y = norm.pdf(x, loc=0, scale=1)
print("Gaussian Distribution: ", y)
# plt.plot(x, y, label="Gaussian")
# plt.title("Gaussian Distribution")
# plt.show()

# Binomial Distribution
n, p = 10, 0.5
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)
print("Binomial Distribution: ", y)
# plt.bar(x, y, label="Binomial")
# plt.title("Binomial Distribution")
# plt.show()

# Poisson Distribution
lam =3
x = np.arange(0, 10)
y = poisson.pmf(x, lam)
print("Poisson Distribution: ", y)
# plt.bar(x, y, label="Poisson")
# plt.title("Poisson Distribution")
# plt.show()
