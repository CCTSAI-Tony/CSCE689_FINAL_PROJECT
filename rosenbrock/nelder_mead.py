import scipy.optimize
from rosenbrock.method import Method


class NelderMead(Method):
    '''
    NelderMead class accepts 2 arguments, which are function and first guess tuple coordinate.
    It inherits from Method class.
    '''

    def optimize(self):
        '''
        the main func to run the optomization test
        '''
        self.res = scipy.optimize.minimize(
            self.func, self._Method__x, method='Nelder-Mead', callback=self.record)
