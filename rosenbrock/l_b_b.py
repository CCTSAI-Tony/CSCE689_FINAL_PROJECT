import scipy.optimize
from rosenbrock.method import Method


class L_BFGS_B(Method):
    '''
    L_BFGS_B class accepts 2 arguments, which are function and first guess tuple coordinate.
    It inherits from Method class.
    '''

    def optimize(self):
        self.res = scipy.optimize.minimize(
            self.func, self._Method__x, method='L-BFGS-B', callback=self.record)
