import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import matplotlib.animation as animation

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

# NEW: Here we go!
alpha = tf.Variable(0.3)
beta = tf.Variable(0.3)

u = 0
v = 0

xs_tf = tf.constant(xs, dtype=tf.float32)
ys_tf = tf.constant(ys, dtype=tf.float32)

alphas = []
betas = []
neg_sum_squared_errors = []

step = 18
# Iterations that we need to climb the hill.
for i in range(1000):

    if i % step == 0:
        # Set random flick.
        u = np.random.normal(scale = 0.07)
        v = np.random.normal(scale = 0.07)

    # Define our model and its gradient with respect to parameter alpha and beta.
    with tf.GradientTape() as tape:
    
        def model(x):
            return alpha + beta * x

        # Calculate the sum squared error on the data.
        sum_squared_error = tf.reduce_sum(tf.pow(ys_tf - model(xs_tf), 2))

        neg_sum_squared_error = - sum_squared_error

        # Add last alpha, beta and corresponding error to the lists.
        alphas.append(alpha.numpy())
        betas.append(beta.numpy())
        neg_sum_squared_errors.append(neg_sum_squared_error.numpy())

        [dSQE_dalpha, dSQE_dbeta] = tape.gradient(neg_sum_squared_error, [alpha, beta])

        u = u + 0.0003 * dSQE_dalpha
        v = v + 0.0003 * dSQE_dbeta

        # Update particle position.
        alpha.assign_add(u)
        beta.assign_add(v )

# Plot the current points (during the search).
line_animation = ax.plot(alphas, betas, neg_sum_squared_errors, color= "blue")[0]
line_animation_b = ax.scatter(alphas, betas, neg_sum_squared_errors,  marker='o', color= "blue", s= 100)

# update the line plot:
def update(frame):

    low = max(0, frame - (frame % step))
    upper = frame + 2
    
    # Update the current points (during the search).
    line_animation.set_data_3d(alphas[low:upper], betas[low:upper], neg_sum_squared_errors[low:upper])
    
    epsilon = 0.01 # UI thing.
    line_animation_b._offsets3d = (alphas[0:upper:step], betas[0:upper:step], [x + epsilon for x in neg_sum_squared_errors[0:upper:step]])
    
    
    return (line_animation, line_animation_b)

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(alphas), interval=100)

ax.set_title("Hamiltonian Monte Carlo: A particles movement, influenced by the gradient, and random flicks every " + str(step) + " steps")

plt.show()