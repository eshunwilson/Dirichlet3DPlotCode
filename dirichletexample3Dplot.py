#dirichlet example trial

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the Dirichlet distribution
alpha = [2, 3, 4]  # Dirichlet parameters (can be adjusted)
n_samples = 1000   # Number of samples to generate

# Generate random samples from the Dirichlet distribution
samples = np.random.dirichlet(alpha, n_samples)

# Extract components for visualization
x = samples[:, 0]
y = samples[:, 1]
z = samples[:, 2]

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=10)

# Add color bar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Z Component Intensity')

# Add labels and title
ax.set_xlabel('X Component')
ax.set_ylabel('Y Component')
ax.set_zlabel('Z Component')
ax.set_title('Random Samples from a Dirichlet Distribution')

# Show plot
plt.show()