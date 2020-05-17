import scipy.optimize
from rosenbrock.method import Method


class ConjugateGradient(Method):
    '''
    ConjugateGradient class accepts 2 arguments, which are function and first guess tuple coordinate.
    It inherits from Method class.
    '''

    def optimize(self):
        '''
        Optimization of conjugate_gradient method
        '''
        self.res = scipy.optimize.minimize(
            self.func, self._Method__x, method='CG', callback=self.record)
