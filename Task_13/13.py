import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data
x = np.linspace(-4, 4, 100)
y = norm.pdf(x, 0, 1)

# Plot
plt.plot(x, y)
plt.title("Normal Probability Distribution")
plt.xlabel("X values")
plt.ylabel("Probability Density")
plt.show()
