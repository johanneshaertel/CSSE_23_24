import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import matplotlib.animation as animation

np.random.seed(0)

# START: Generate fake-data.
n = 100 # number of observations (was increased here).
xs = np.random.normal(size = n) # random values for x.
mu = 0.9 + xs * 0.4 # mean values for y.

ys = np.random.normal(scale = 0.1, size = n) + mu # final output y.

# END: Generate fake-data.

# Seaching a grid of values for alpha and beta 
# (stupid idea, since this does not scale if we have more parameter).
alphas = [] 
betas = [] 
sum_squared_errors = []

grid = 30

# Model fitting by searching (learning) parameters.
for alpha in np.linspace(-0.5, 1.5, grid): # Parameter 1
    for beta in np.linspace(-0.5, 1.5, grid): # Parameter 2
        
        # Define our model.
        def model(x):
            return alpha + beta * x

        # Calculate the sum squared error on the data.
        sum_squared_error = sum(np.power(ys - model(xs), 2))

        alphas.append(alpha)
        betas.append(beta)
        sum_squared_errors.append(sum_squared_error)
        

# Plot it nicely. Plot the NEGATIVE error (to make it a hill).
fig = plt.figure()
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

# NEW: Here we go!
alpha = tf.Variable(0.0)
beta = tf.Variable(0.0)

xs_tf = tf.constant(xs, dtype=tf.float32)
ys_tf = tf.constant(ys, dtype=tf.float32)

alphas = []
betas = []
neg_sum_squared_errors = []

# Iterations that we need to climb the hill.
for i in range(12):
   
    # Define our model and its gradient with respect to parameter alpha and beta.
    with tf.GradientTape() as t0:
        with tf.GradientTape() as t1:
            with tf.GradientTape() as t2:
        
                def model(x):
                    return alpha + beta * x

                # Calculate the sum squared error on the data.
                sum_squared_error = tf.reduce_sum(tf.pow(ys_tf - model(xs_tf), 2))

                neg_sum_squared_error = - sum_squared_error

                # Add last alpha, beta and corresponding error to the lists.
                alphas.append(alpha.numpy())
                betas.append(beta.numpy())
                neg_sum_squared_errors.append(neg_sum_squared_error.numpy())

                [dSQE_dalpha, dSQE_dbeta] = t2.gradient(neg_sum_squared_error, [alpha, beta])
                
            [dSQE_dbeta_dbeta] = t1.gradient(dSQE_dbeta, [beta])
        [dSQE_dalpha_dalpha] = t0.gradient(dSQE_dalpha, [alpha])

        # Update alpha and beta (assign_sub subtracts value from this variable).
        alpha.assign_add(0.001 * dSQE_dalpha)
        beta.assign_add(0.001 * dSQE_dbeta)

# Plot the current point.
ax.plot(alphas, betas, neg_sum_squared_errors,  marker='o', color= "black", markersize=9)

alphas = np.linspace(-0.5, 1.5, grid)
approx = dSQE_dalpha_dalpha.numpy() * np.power(alpha.numpy() - alphas, 2) * 0.5
ax.plot(alphas, np.repeat(beta.numpy(), grid), approx, color= "gold", linewidth=3)

betas = np.linspace(-0.5, 1.5, grid)
approx = dSQE_dbeta_dbeta.numpy() * np.power(beta.numpy() - betas, 2) * 0.5
ax.plot(np.repeat(alpha.numpy(), grid), betas, approx, color= "gold", linewidth=3)

plt.show()