import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# START: Generate fake-data.
n = 20 # number of observations.
xs = np.random.normal(size = n) # random values for x.
mu = 0.9 + xs * 0.4 # mean values for y.

ys = np.random.normal(scale = 0.1, size = n) + mu # final output y.

# END: Generate fake-data.

# Plot it nicely.
fig, ax = plt.subplots()
ax.plot(xs, ys, marker='o', linestyle='', color='black')
plt.show()