# By Frank
from rosenbrock.nelder_mead import NelderMead
from rosenbrock.conjugate_gradient import ConjugateGradient
from rosenbrock.l_b_b import L_BFGS_B
from rosenbrock.rosenbrock import rosenbrock
from rosenbrock.plot import plot

import time


def print_result(class1, class2, class3):

    print("Frank's Optimization Research")
    print("| Method             | Iterations | Time (ms) |")
    print("+--------------------+------------+-----------+")
    print("| Nelder-Mead        |", '{:10d}'.format(class1.iteration), "|", '{:9.2f}'.format(1E3*class1.time), "|")
    print("| Conjugate Gradient |", '{:10d}'.format(class2.iteration), "|", '{:9.2f}'.format(1E3*class2.time), "|")
    print("| L-BFGS-B           |", '{:10d}'.format(class3.iteration), "|", '{:9.2f}'.format(1E3*class3.time), "|")


def main():

    total1 = time.perf_counter()
    nel_md = NelderMead(rosenbrock, [(-3, -4)])
    c_grad = ConjugateGradient(rosenbrock, [(-3, -4)])
    l_b_b = L_BFGS_B(rosenbrock, [(-3, -4)])
    print_result(nel_md, c_grad, l_b_b)
    total2 = time.perf_counter()
    print("| Total Execution Time (w/o plot):    ", '{:5.2f}'.format(1E3*(total2-total1)), "|")
    plot(nel_md, c_grad, l_b_b)

if __name__ == '__main__':
    main()
