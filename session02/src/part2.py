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

# Define our model's alpha and beta (we need to explore alternatives here).
alpha = 0.3
beta = -0.4

mu = alpha + beta * xs

# Ceck how good it fits: Calculate the sum squared error on the data.
sum_squared_error = sum(np.power(ys - mu, 2))

# Plot it nicely.
fig, ax = plt.subplots(figsize=(10,8))

# Plot nice line.
xs_line = np.linspace(-3, 3, 100)
ys_line = alpha + beta * xs_line
ax.plot(xs_line, ys_line, color='blue')

ax.set_xlabel('Number of Public Methods for a Class (xs)')
ax.set_ylabel('Number of Comments for a Class (ys)')

# Plot the error of each observations.
for i in range(n):
    ax.plot([xs[i], xs[i]], [ys[i], mu[i]], color='red', linestyle='--')

ax.plot(xs, ys, marker='o', linestyle='', color='black')

ax.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
ax.axvline(x=0, color='black', linestyle='--', linewidth=0.5)

ax.set_title(f"Error Function: Sum squared error: {np.round(sum_squared_error, 2)}")

plt.show()
