import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.ticker import LogLocator
from rosenbrock.nelder_mead import NelderMead
from rosenbrock.conjugate_gradient import ConjugateGradient
from rosenbrock.l_b_b import L_BFGS_B
from rosenbrock.rosenbrock import rosenbrock



def plot(class1,class2,class3):
    x_min = min(class1.x_min, class2.x_min, class3.x_min)
    x_max = max(class1.x_max, class2.x_max, class3.x_max)
    y_min = min(class1.y_min, class2.y_min, class3.y_min)
    y_max = max(class1.y_max, class2.y_max, class3.y_max)
    num_points = 1000
    x = np.linspace(x_min-1, x_max+1, num_points)
    y = np.linspace(y_min-1, y_max+1, num_points)
    X, Y = np.meshgrid(x, y)
    Z = rosenbrock([X,Y])
    normalize = colors.LogNorm(vmin=Z.min(), vmax=Z.max())
    plt.plot(class1.x_iterates, class1.y_iterates, 'ro:', linewidth=3, label="Nelder-Mead")
    plt.plot(class2.x_iterates, class2.y_iterates, 'mo--', linewidth=3, label="Conjugate Gradient")
    plt.plot(class3.x_iterates, class3.y_iterates, 'co-', linewidth=3, label="L-BFGS-B")
    plt.contourf(X, Y, Z, norm=normalize, cmap='cividis', locator=LogLocator(base=2, numticks=20))
    plt.plot(-3, -4, 'kX', markersize=12, markeredgecolor='white', label='Starting Point')
    plt.plot(1, 1, 'wX', markersize=12, markeredgecolor='black', label='Global Minimum')
    plt.legend(loc=2)
    plt.title('Comparison of Three Optimization Methods\nOptimizing Over the Rosenbrock Function')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()
