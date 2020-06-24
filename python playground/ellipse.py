import numpy as np
import matplotlib.pyplot as plt
import math


A = np.array([
    [1, 2],
    [2, 2]
])

i = np.array([[1], [0]])

n = 72
degree = 2 * math.pi / n
rotation_matrix = np.array([
    [math.cos(degree), -1 * math.sin(degree)],
    [math.sin(degree), math.cos(degree)]
])

current = i
transformed_current = A @ i
for j in range(n):
    plt.plot(current[0][0], current[1][0], 'bo')
    plt.plot(transformed_current[0][0], transformed_current[1][0], 'ro')
    current = rotation_matrix @ current
    transformed_current = A @ current

plt.axis('equal')
plt.show()
