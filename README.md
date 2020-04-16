• Introduction

The purpose of the software is to compare three optimization algorithms and their performaces based on Rosenbrock function,

and the three algorithms are called Nelder-Mead, Conjugate Gradient and L-BFGS-B.

The Rosenbrock function is defined as: $$f_{Rosen}(x,y) = (100(y - x^2)^2 + (1-x)^2$$.

Onee the software being executed, it prints out a table which states how many iterations each algorithm take,

and overall runtime respectively. It also outputs a plot that includes different routes of the three algoriths

which all start form point (3,4) and terminate at point (1,1) as the minimum location of the Rosenbrock fuction.

At first, the original version of the code does not follow object oriented design, the main() function are cramed with

all of the logic code which is not easy for managing and it doesn't align PEP8 guidelines as naming rule, formatting, etc.

Another big problem is that it does't have its own test suite, which is needed to be built from scratch.




• Modifications and Improvements

orginal:

| Nelder-Mead        |         75 |      4.62 |

| Conjugate Gradient |         37 |      4.40 |

| L-BFGS-B           |         29 |      1.56 |

| Total Execution Time (w/o plot):     206.67 |

modified:

| Nelder-Mead        |         75 |      5.02 |

| Conjugate Gradient |         37 |      5.50 |

| L-BFGS-B           |         29 |      1.93 |

| Total Execution Time (w/o plot):     12.84 |






• Conclusion
