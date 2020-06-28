import numpy as np
import matplotlib.pyplot as plt

# f(x1, x2) = a * x1^2 + b * x1x2 + c * x2^2
a = 6
b = 1
c = 2

x1_range = np.linspace(-2, 2, 30)
x2_range = np.linspace(-2, 2, 30)

x1, x2 = np.meshgrid(x1_range, x2_range)
z = a * x1**2 + b * x1*x2 + c * x2**2

ax = plt.axes(projection='3d')
ax.plot_surface(x1, x2, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none', alpha=0.9)

A = np.array([
    [a, b/2],
    [b/2, c]
])

eig_values = np.linalg.eigvals(A)
l1 = eig_values[0]
l2 = eig_values[1]

b_signed = '%s%s' % ('' if b < 0 else '+', '' if b == 1 else str(b))
c_signed = '%s%s' % ('' if c < 0 else '+', '' if c == 1 else str(c))

p1 = '%dx_1^2' % a if a != 0 else ''
p2 = '%sx_1x_2' % b_signed if b != 0 else ''
p3 = '%sx_2^2' % c_signed if c != 0 else ''


print(l1)
print(l2)

eps = 10**-7
if l1 > eps and l2 > eps:
    stat = 'Positive Definite'
elif l1 < -eps and l2 < -eps:
    stat = 'Negative Definite'
elif l1 > eps > l2 > -eps or \
        l2 > eps > l1 > -eps:
    stat = 'Positive Semidefinite'
elif l1 < -eps < l2 < eps or \
        l2 < -eps < l1 < eps:
    stat = 'Negative Semidefinite'
else:
    stat = 'Indefinite'

title = '$f(x_1, x_2)=%s%s%s$\nEigenvalues of A = %.2f, %.2f\n%s' % (p1, p2, p3, l1, l2, stat)
plt.title(title, fontdict={'fontsize': '18'}, pad=35)

ax.set_xlabel('x1', fontdict={'fontsize': '15'}, labelpad=15)
ax.set_ylabel('x2', fontdict={'fontsize': '15'}, labelpad=15)
ax.set_zlabel('z', fontdict={'fontsize': '15'}, labelpad=15)
plt.show()

