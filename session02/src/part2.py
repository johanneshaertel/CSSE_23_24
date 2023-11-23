import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# START: Generate fake-data.
n = 20 # number of observations.
xs = np.random.normal(size = n) # random values for x.
mu = 0.9 + xs * 0.4 # mean values for y.

ys = np.random.normal(scale = 0.1, size = n) + mu # final output y.

# END: Generate fake-data.

# Define our model.
alpha = 0.05
beta = -0.4

def model(x):
    return alpha + beta * x

# Plot it nicely.
fig, ax = plt.subplots()

# Plot nice line.
xs_line = np.linspace(-3, 3, 100)
ys_line = model(xs_line)
ax.plot(xs_line, ys_line, color='blue')

# Plot the error of each observations.
for i in range(n):
    ax.plot([xs[i], xs[i]], [ys[i], model(xs[i])], color='red', linestyle='--')

ax.plot(xs, ys, marker='o', linestyle='', color='black')

# Calculate the sum squared error on the data.
sum_squared_error = sum(np.power(ys - model(xs), 2))

ax.set_title(f"Sum squared error: {np.round(sum_squared_error, 2)}")

plt.show()
