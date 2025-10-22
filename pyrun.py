import numpy as np

# Define arrays
x = np.array([3, 7, 1, 9, 5])
y = np.array([2, 7, 3, 8, 6])

# Find indices where x >= y
indices = np.where(x >= y)

# Display results
print("Array x:", x)
print("Array y:", y)
print("Indices where x >= y:", indices[0])
