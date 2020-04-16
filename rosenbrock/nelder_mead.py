import numpy as np
import scipy.optimize
import time


class NelderMead():
    '''
    NelderMead class accepts 2 arguments, which are function and first guess tuple coordinate.
    It includes self.x fild which lists out all the intermediate guess data
    The self.iteration field record the total times of loops.
    '''

    def __init__(self, func, x0):
        self.func = func
        self.x = np.array(x0)
        self.time = 0
        self.iteration = 0
        self.process()

    def record(self, xk):
        self.x = np.vstack((self.x, (xk)))

    def optimize(self):
        self.res = scipy.optimize.minimize(
            self.func, self.x, method='Nelder-Mead', callback=self.record)

    def process(self):
        self.start = time.perf_counter()
        self.optimize()
        self.end = time.perf_counter()
        self.time = self.end - self.start
        self.iteration = len(self.x)
        self.x_iterates = np.array([xk[0] for xk in self.x])
        self.y_iterates = np.array([xk[1] for xk in self.x])
        self.x_min = np.amin(self.x_iterates)
        self.x_max = np.amax(self.x_iterates)
        self.y_min = np.amin(self.y_iterates)
        self.y_max = np.amax(self.y_iterates)
