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
        '''
        Builds up attributes and properties
        Auto run the self.process() method
        '''
        self.func = func
        self.__x = np.array(x0)
        self.time = 0
        self.__iteration = 0
        self.process()

    @property
    def x(self):
        """Getter for '__x'."""
        return self.__x

    @property
    def iteration(self):
        """Getter for '__iteration'."""
        return self.__iteration

    def record(self, xk):
        '''
        Adding intermediate result to self.__x property
        '''
        self.__x = np.vstack((self.__x, (xk)))

    def optimize(self):
        '''
        the main func to run the optomization test
        '''
        self.res = scipy.optimize.minimize(
            self.func, self.__x, method='Nelder-Mead', callback=self.record)

    def process(self):
        '''
        Implementing self.optomize() method and do some computations to store or alter
        some attributes.
        '''
        self.start = time.perf_counter()
        self.optimize()
        self.end = time.perf_counter()
        self.time = self.end - self.start
        self.__iteration = len(self.__x)
        self.x_iterates = np.array([xk[0] for xk in self.__x])
        self.y_iterates = np.array([xk[1] for xk in self.__x])
        self.x_min = np.amin(self.x_iterates)
        self.x_max = np.amax(self.x_iterates)
        self.y_min = np.amin(self.y_iterates)
        self.y_max = np.amax(self.y_iterates)
