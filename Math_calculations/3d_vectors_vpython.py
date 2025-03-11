import numpy as np
from vpython import canvas, arrow, vector


# Define a function for creating the 3D vector field
def vector_field(X, Y, Z, t):
    """
    Create a vector field that evolves over time t.
    Example: Circular motion around the z-axis.
    """
    U = -Y * np.cos(t) + Z * np.sin(t)
    V = X * np.cos(t) - Z * np.sin(t)
    W = X * np.sin(t) + Y * np.cos(t)

    return U, V, W


# Define the grid
X = np.linspace(-2, 2, 5)
Y = np.linspace(-2, 2, 5)
Z = np.linspace(-2, 2, 5)
X, Y, Z = np.meshgrid(X, Y, Z)
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# Define a function for creating the 3D vector field
def vector_field(X, Y, Z, t):
    """
    Create a vector field that evolves over time t.
    In this example, we use a rotating vector field (simplified example).

    X, Y, Z: Coordinates of the grid
    t: Time parameter (for animation)

    Returns: Three arrays representing the vector components in the X, Y, and Z directions
    """
    # Example: Circular/rotational motion around the z-axis
    U = -Y * np.cos(t) + Z * np.sin(t)
    V = X * np.cos(t) - Z * np.sin(t)
    W = X * np.sin(t) + Y * np.cos(t)

    return U, V, W


# Set up the grid (you can adjust the grid size and spacing as needed)
X = np.linspace(-2, 2, 10)  # X-axis from -2 to 2 with 10 points
Y = np.linspace(-2, 2, 10)  # Y-axis from -2 to 2 with 10 points
Z = np.linspace(-2, 2, 10)  # Z-axis from -2 to 2 with 10 points
X, Y, Z = np.meshgrid(X, Y, Z)  # Create the 3D grid

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a quiver plot for the vector field
# Initially, we set the field at t = 0
t_init = 0
U, V, W = vector_field(X, Y, Z, t_init)
quiver = ax.quiver(X, Y, Z, U, V, W)

# Set the plot limits and labels
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D Vector Field")


# Animation function to update the vector field over time
def update(t):
    # Recalculate the vector field at the new time t
    U, V, W = vector_field(X, Y, Z, t)

    # Update the quiver plot
    quiver.set_UVC(U, V, W)
    return quiver,


# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), interval=50)
ani = FuncAnimation(fig, )
# Display the animation
plt.show()
"""
# Create a canvas for 3D visualization
scene = canvas(title="3D Vector Field", width=800, height=600, center=vector(0, 0, 0), background=color.white)


# Function to create a vector field plot at a given time t
def plot_vector_field_at_time(t):
    # Clear previous arrows
    scene.objects.clear()

    # Compute the vector components at time t
    U, V, W = vector_field(X, Y, Z, t)

    # Create arrows representing the vector field
    arrows = []
    for i in range(len(X)):
        for j in range(len(Y)):
            for k in range(len(Z)):
                # Get the components of the vector
                vector_start = vector(X[i, j, k], Y[i, j, k], Z[i, j, k])
                vector_end = vector(X[i, j, k] + U[i, j, k], Y[i, j, k] + V[i, j, k], Z[i, j, k] + W[i, j, k])
                arrows.append(
                    arrow(pos=vector_start, axis=vector_end - vector_start, color=color.blue, shaftwidth=0.05))

    return arrows


# Plot vector fields at t = 0, t = t1, and t = ∞
t1 = np.pi  # Set a specific time point (can be adjusted)
t_infinity = 2 * np.pi  # A large value to simulate "infinity"

# Plot for t = 0
plot_vector_field_at_time(0)

# Wait for user to press a key to change time
scene.caption = "Press 't1' to show the vector field at t = t1"


# Set up event listener for key presses
def key_listener(evt):
    if evt.key == 't':
        # Plot for t = t1
        plot_vector_field_at_time(t1)
        scene.caption = f"Vector field at t = {t1}"


# Add key listener for interactive change of time
scene.bind('keydown', key_listener)

# Wait for 't' press for t = t1
scene.waitfor('keydown')

# Once 't1' is pressed, show t = infinity field
plot_vector_field_at_time(t_infinity)
scene.caption = f"Vector field at t = {t_infinity} (Approaching infinity)"

# Keep the window open until closed by the user
scene.waitfor('close')