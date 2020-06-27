import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [7, 2, 0],
    [1, -2, 3]
])

c = 40
u = np.linspace(0, np.pi, c)
v = np.linspace(0, 2 * np.pi, c)

x = np.outer(np.sin(u), np.sin(v))
y = np.outer(np.sin(u), np.cos(v))
z = np.outer(np.cos(u), np.ones_like(v))

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2)

for i in range(c):
    ax1.plot(x[i], y[i], z[i], 'b')
    v = np.vstack((x[i], y[i], z[i]))
    t = A @ v
    ax2.plot(t[0], t[1], 'r')


AtA = A.transpose() @ A
eig = np.linalg.eig(AtA)

biggest_index = 0
smallest_index = 0
for i in 1, 2:
    if 10**-10 < abs(eig[0][i]) > abs(eig[0][biggest_index]):
        biggest_index = i
    if abs(eig[0][smallest_index]) > abs(eig[0][i]) > 10**-10:
        smallest_index = i

v1 = eig[1][:, biggest_index]
v2 = eig[1][:, smallest_index]

Av1 = A @ v1
Av2 = A @ v2

ax2.quiver(0, 0, Av1[0], Av1[1], color='b', angles='xy', scale_units='xy', scale=1, label='$Av_1$')
ax2.quiver(0, 0, Av2[0], Av2[1], color='g', angles='xy', scale_units='xy', scale=1, label='$Av_2$')

ax2.grid()
ax2.axis('equal')
plt.legend()
plt.show()
