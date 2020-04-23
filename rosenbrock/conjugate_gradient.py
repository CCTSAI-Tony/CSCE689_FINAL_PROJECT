import scipy.optimize
from rosenbrock.nelder_mead import NelderMead


class ConjugateGradient(NelderMead):
    '''
    ConjugateGradient class accepts 2 arguments, which are function and first guess tuple coordinate.
    It inherits from NelderMead class.
    '''

    def optimize(self):
        '''
        Optimization of conjugate_gradient method
        '''
        self.res = scipy.optimize.minimize(
            self.func, self._NelderMead__x, method='CG', callback=self.record)
