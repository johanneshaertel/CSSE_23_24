import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 20 # number of observations.

xs = np.random.normal(size = n) # random values for x.

beta = 0.4
alpha = 0.2

mu = alpha + (beta * xs)

sigma = 0.1

ys = mu + np.random.normal(scale = sigma, size = n)

fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(xs, ys, marker='o', color='black')

ax.set_xlabel('Number of Public Methods for a Class (xs)')
ax.set_ylabel('Number of Comments for a Class (ys)')

ax.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
ax.axvline(x=0, color='black', linestyle='--', linewidth=0.5)

plt.show()