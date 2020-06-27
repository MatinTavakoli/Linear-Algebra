import numpy as np
import matplotlib.pyplot as plt
import math


A = np.array([
    [1, 0],
    [2, 2],
    [3, -1]
])

i = np.array([[1], [0]])

n = 100
degree = 2 * math.pi / n
rotation_matrix = np.array([
    [math.cos(degree), -1 * math.sin(degree)],
    [math.sin(degree), math.cos(degree)]
])

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

current = i
transformed_current = A @ i
for j in range(n):
    ax1.plot(current[0][0], current[1][0], 'bo')
    ax2.scatter(transformed_current[0][0], transformed_current[1][0], transformed_current[2][0])
    current = rotation_matrix @ current
    transformed_current = A @ current

AtA = A.transpose() @ A
eig = np.linalg.eig(AtA)

v1 = eig[1][:, 0]
v2 = eig[1][:, 1]

Av1 = A @ v1
Av2 = A @ v2

ax2.quiver(0, 0, 0, Av1[0], Av1[1], Av1[2], color='b', label='$Av_1$', pivot='tail')
ax2.quiver(0, 0, 0, Av2[0], Av2[1], Av2[2], color='g', label='$Av_2$', pivot='tail')

plt.legend()
ax1.axis('equal')
plt.show()
