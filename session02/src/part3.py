import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# START: Generate fake-data (simulation).
n = 100 # number of observations.
xs = np.random.normal(size = n) # random values for x.
mu = 0.9 + xs * 0.4 # mean values for y.
sigma = 0.1

ys = np.random.normal(scale = sigma, size = n) + mu # final output y.

# END: Generate fake-data  (simulation).

# Seaching a grid of values for alpha and beta 
# (stupid idea, since this does not scale if we have more parameter).
alphas = [] 
betas = [] 
sum_squared_errors = []

grid = 30

# Model fitting by searching (learning) parameters.
for alpha in np.linspace(-1, 2, grid): # Parameter 1
    for beta in np.linspace(-1, 2, grid): # Parameter 2
        
        # Define our model.
        def model(x):
            return alpha + beta * x

        # Calculate the sum squared error on the data.
        sum_squared_error = sum(np.power(ys - model(xs), 2))

        alphas.append(alpha)
        betas.append(beta)
        sum_squared_errors.append(sum_squared_error)
        

# Plot it nicely. Plot the NEGATIVE error (to make it a hill).
fig = plt.figure(figsize=(20,15))
ax = fig.add_subplot(projection='3d')

# Numply, reshaping madness.
alphas = np.array(alphas).reshape(grid, grid)
betas = np.array(betas).reshape(grid, grid)
neg_sum_squared_errors = - np.array(sum_squared_errors).reshape(grid, grid)

# Plot hill and contour.
ax.plot_surface(alphas, betas, neg_sum_squared_errors, edgecolor='red', lw=0.5, rstride=3, cstride=3, alpha=0.3)
ax.contour(alphas, betas, neg_sum_squared_errors, zdir='z', offset=np.min(neg_sum_squared_errors), cmap='coolwarm')

# Add nice lables to the plot.
ax.set_xlabel('alphas (parameter)')
ax.set_ylabel('betas (parameter)')
ax.set_zlabel('sum squared error (negative)')

ax.set_title('Grid Search: The sum squared error as a function of alpha and beta')

plt.show()