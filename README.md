• Introduction




The purpose of the software is to compare three optimization algorithms and their performaces based on Rosenbrock function,

and the three algorithms are called Nelder-Mead, Conjugate Gradient and L-BFGS-B.

The Rosenbrock function is defined as: $$f_{Rosen}(x,y) = (100(y - x^2)^2 + (1-x)^2$$.

Onee the software being executed, it prints out a table which states how many iterations each algorithm take,

and overall runtime respectively. It also outputs a plot that includes different results of the three algoriths

which all start form point (-3,-4) and terminate at point (1,1) as the minimum location of the Rosenbrock fuction.

At first, the original version of the code does not follow object oriented design, the main() function are cramed with

all of the logic code which is not easy for managing and it doesn't align PEP8 guidelines as naming rule, formatting, etc.

Another big problem is that it does't have its own test suite, which is needed to be built from scratch.

In this project, I need to find a way to refactoring the code, so it can be maintained and managed easily in the future.









• Modifications and Improvements




Applying the object oriented design, I choose to buld up three classes corresponding to three different optomization

algorithms.

Using this design, we can create some fields to record their data status automatically and don't worry about

any disturbance by poor naming source code, ex: same name variables.

I also use inheritance style to manage similiar classes, ex: Conjugate Gradient and L-BFGS-B all inherit from Nelder-Mead.

By this manner, we can save some code space from repeated function code.

Along the way, I put the record function into the class which can take the object oriented advantage to comunicate the class's

property directly.

Evetually, I modulize the soure code into different fuctions and classes to make them already for test.

In the original source code, it's kind of the pain to fingure out how the plot be actually painted, so I put all the

code related to plot into one fuction called plot().

By dong so, we can use simple one fuction call to print out the plot.

Regarding to test suite, I build up 5 unitests.

First is test_rosenbrock to test if rosenbrock function is correct, and followed by three classes test.

I check each optimization's class property by comparing with the original source code's behavior,

like how many iterations it take, and what all the intermediate results are.

Lastly, I build up a test_print_result to check the correct output lines via regular expression,

and edit the whole source code followed the PEP8 guidelines.









• Conclusion




In this project, we learn how to turn a plain source code into a maintainable module, and build a test suite

to verify that the functionalty is the sane as the original source code.

After this changing, from the output data we can find that the total process time withot plot is less 10 times than

the original source code!

Below are the output console data of original and modefied source code.


orginal:

| Method             | Iterations | Time (ms) |

+--------------------+------------+-----------+

| Nelder-Mead        |         75 |      4.62 |

| Conjugate Gradient |         37 |      4.40 |

| L-BFGS-B           |         29 |      1.56 |

| Total Execution Time (w/o plot):     206.67 |

modified:

| Method             | Iterations | Time (ms) |

+--------------------+------------+-----------+

| Nelder-Mead        |         75 |      5.02 |

| Conjugate Gradient |         37 |      5.50 |

| L-BFGS-B           |         29 |      1.93 |

| Total Execution Time (w/o plot):     12.84 |
