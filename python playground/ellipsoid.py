import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [1, 0, 0.5],
    [0, 1, 0],
    [0, 0, 1]
])

c = 40
u = np.linspace(0, np.pi, c)
v = np.linspace(0, 2 * np.pi, c)

x = np.outer(np.sin(u), np.sin(v))
y = np.outer(np.sin(u), np.cos(v))
z = np.outer(np.cos(u), np.ones_like(v))

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

for i in range(c):
    ax1.plot(x[i], y[i], z[i], 'b')
    v = np.vstack((x[i], y[i], z[i]))
    t = A @ v
    ax2.plot(t[0], t[1], t[2], 'r')


def axis_equal(ax):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:, 1] - extents[:, 0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)


axis_equal(ax2)
plt.show()
