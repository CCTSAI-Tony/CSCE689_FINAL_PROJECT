# By Frank

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
import matplotlib.colors as colors
import time

global x

def F(x):
    return pow(1-x[0],2) + 100*pow(x[1] - pow(x[0],2),2)

def record(xk):
    global x
    x.append(xk)

def main():
    total1 = time.perf_counter()
    print("Frank's Optimization Research")
    global x
    x = [(-3, -4)]

    s = time.perf_counter()
    res = scipy.optimize.minimize(F, x, method='Nelder-Mead', callback=record)
    e = time.perf_counter()
    nmt = e-s
    nmi = len(x)

    x_iterates = [xk[0] for xk in x]
    y_iterates = [xk[1] for xk in x]
    plt.plot(x_iterates, y_iterates, 'ro:', linewidth=3, label="Nelder-Mead")

    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    for i in range(len(x_iterates)):
        if x_iterates[i] < x_min:
            x_min = x_iterates[i]

    for i in range(len(x_iterates)):
        if x_iterates[i] > x_max:
            x_max = x_iterates[i]

    for i in range(len(y_iterates)):
        if y_iterates[i] < y_min:
            y_min = y_iterates[i]

    for i in range(len(y_iterates)):
        if y_iterates[i] > y_max:
            y_max = y_iterates[i]

    x = [(-3, -4)]
    s = time.perf_counter()
    res = scipy.optimize.minimize(F, x, method='CG', callback=record)
    e = time.perf_counter()
    cgt = e-s
    cgi = len(x)

    x_iterates = [xk[0] for xk in x]
    y_iterates = [xk[1] for xk in x]
    plt.plot(x_iterates, y_iterates, 'mo--', linewidth=3, label="Conjugate Gradient")
    
    for i in range(len(x_iterates)):
        if x_iterates[i] < x_min:
            x_min = x_iterates[i]

    for i in range(len(x_iterates)):
        if x_iterates[i] > x_max:
            x_max = x_iterates[i]

    for i in range(len(y_iterates)):
        if y_iterates[i] < y_min:
            y_min = y_iterates[i]

    for i in range(len(y_iterates)):
        if y_iterates[i] > y_max:
            y_max = y_iterates[i]

    x = [(-3, -4)]
    s = time.perf_counter()
    res = scipy.optimize.minimize(F, x, method='L-BFGS-B', callback=record)
    e = time.perf_counter()
    lbt = e-s
    lbi = len(x)

    print("| Method             | Iterations | Time (ms) |")
    print("+--------------------+------------+-----------+")
    print("| Nelder-Mead        |", '{:10d}'.format(nmi), "|", '{:9.2f}'.format(1E3*nmt), "|")
    print("| Conjugate Gradient |", '{:10d}'.format(cgi), "|", '{:9.2f}'.format(1E3*cgt), "|")
    print("| L-BFGS-B           |", '{:10d}'.format(lbi), "|", '{:9.2f}'.format(1E3*lbt), "|")

    x_iterates = [xk[0] for xk in x]
    y_iterates = [xk[1] for xk in x]
    plt.plot(x_iterates, y_iterates, 'co-', linewidth=3, label="L-BFGS-B")

    num_points = 1000
    for i in range(len(x_iterates)):
        if x_iterates[i] < x_min:
            x_min = x_iterates[i]

    for i in range(len(x_iterates)):
        if x_iterates[i] > x_max:
            x_max = x_iterates[i]

    for i in range(len(y_iterates)):
        if y_iterates[i] < y_min:
            y_min = y_iterates[i]

    for i in range(len(y_iterates)):
        if y_iterates[i] > y_max:
            y_max = y_iterates[i]

    x = np.linspace(x_min-1, x_max+1, num_points)
    y = np.linspace(y_min-1, y_max+1, num_points)

    X, Y = np.meshgrid(x, y)
    Z = F([X,Y])

    total2 = time.perf_counter()
    print("| Total Execution Time (w/o plot):    ", '{:5.2f}'.format(1E3*(total2-total1)), "|")

    normalize = colors.LogNorm(vmin=Z.min(), vmax=Z.max())
    plt.contourf(X, Y, Z, norm=normalize, cmap='cividis', locator=LogLocator(base=2, numticks=20))

    plt.plot(-3, -4, 'kX', markersize=12, markeredgecolor='white', label='Starting Point')
    plt.plot(1, 1, 'wX', markersize=12, markeredgecolor='black', label='Global Minimum')

    plt.legend(loc=2)
    plt.title('Comparison of Three Optimization Methods\nOptimizing Over the Rosenbrock Function')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.show()

if __name__ == '__main__':
    main()