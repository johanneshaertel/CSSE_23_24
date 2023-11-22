import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 100 # number of observations (was increased here).
xs = np.random.normal(size = n) # random values for x.
mu = 0.9 + xs*0.4 # mean values for y.

ys = np.random.normal(scale = 0.1, size = n) + mu # final output y.

# Define our model fitting.

alphas = [] 
betas = [] 
sum_squared_errors = []

for alpha in np.linspace(-1, 2, 30): # Parameter 1
    for beta in np.linspace(-1, 2, 30): # Parameter 2
        def model(x):
            return alpha + beta * x

        sum_squared_error = sum(np.power(ys - model(xs), 2))

        alphas.append(alpha)
        betas.append(beta)
        sum_squared_errors.append(- sum_squared_error)
        

# Plot it nicely.
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot the NEGATIVE error (to make it a hill).
ax.scatter(alphas, betas, sum_squared_errors, marker = 'o', color= "red")

ax.set_xlabel('alpha')
ax.set_ylabel('beta')
ax.set_zlabel('sum squared error (negative)')

plt.show()




# 


# https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html#sphx-glr-gallery-mplot3d-contour3d-3-py
