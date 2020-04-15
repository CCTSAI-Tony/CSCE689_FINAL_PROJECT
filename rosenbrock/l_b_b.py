import numpy as np
import scipy.optimize
import time


class L_BFGS_B():
    def __init__(self, func, x0):
        self.func = func
        self.x = x0
        self.time = 0
        self.iteration = 0
        self.x_min = 0
        self.x_max = 0
        self.y_min = 0
        self.y_max = 0
        self.x_iterates = []
        self.y_iterates = []
        self.optimize()

    def record(self,xk):
        self.x.append(xk)

    def optimize(self):
        self.start = time.perf_counter()
        self.res = scipy.optimize.minimize(self.func, self.x, method='L-BFGS-B', callback=self.record)
        self.end = time.perf_counter()
        self.time = self.end - self.start
        self.iteration = len(self.x)
        self.x_iterates = [xk[0] for xk in self.x]
        self.y_iterates = [xk[1] for xk in self.x]

        def find_x_min():
            for i in range(len(self.x_iterates)):
                if self.x_iterates[i] < self.x_min:
                    self.x_min = self.x_iterates[i]
            return self.x_min

        def find_x_max():
            for i in range(len(self.x_iterates)):
                if self.x_iterates[i] > self.x_max:
                    self.x_max = self.x_iterates[i]
            return self.x_max

        def find_y_min():
            for i in range(len(self.y_iterates)):
                if self.y_iterates[i] < self.y_min:
                    self.y_min = self.y_iterates[i]
            return self.y_min

        def find_y_max():
            for i in range(len(self.y_iterates)):
                if self.y_iterates[i] > self.y_max:
                    self.y_max = self.y_iterates[i]
            return self.y_max


        self.x_min = find_x_min()
        self.x_max = find_x_max()
        self.y_min = find_y_min()
        self.y_mxx = find_y_max()
