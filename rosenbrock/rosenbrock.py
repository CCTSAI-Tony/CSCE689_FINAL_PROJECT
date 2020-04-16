# import numpy as np


def rosenbrock(x):
    '''
    Pass in the coordinate [(x,y)] and return the rosenbrock function result.
    '''
    return (pow(1-x[0], 2) + 100*pow(x[1] - pow(x[0], 2), 2))
