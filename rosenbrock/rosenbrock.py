# import numpy as np

def rosenbrock(x):
    # return np.array(pow(1-x[0],2) + 100*pow(x[1] - pow(x[0],2),2))
    return (pow(1-x[0],2) + 100*pow(x[1] - pow(x[0],2),2))
