import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# START: Generate fake-data (simulation).
n = 20 # number of observations.
xs = np.random.normal(size = n) # random values for x.
mu = 0.9 + xs * 0.4 # mean values for y.
sigma = 0.1

ys = np.random.normal(scale = sigma, size = n) + mu # final output y.

# END: Generate fake-data  (simulation).

# Plot it nicely.
fig, ax = plt.subplots(figsize=(10,8))

ax.plot(xs, ys, marker='o', linestyle='', color='black')

ax.set_xlabel('Number of Public Methods (xs)')
ax.set_ylabel('Number of Comments (ys)')

ax.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
ax.axvline(x=0, color='black', linestyle='--', linewidth=0.5)

ax.set_title('Simulated Data')

plt.show()