import scipy.optimize
from rosenbrock.nelder_mead import NelderMead


class L_BFGS_B(NelderMead):
    '''
    L_BFGS_B class accepts 2 arguments, which are function and first guess tuple coordinate.
    It inherits from NelderMead class.
    '''

    def optimize(self):
        self.res = scipy.optimize.minimize(
            self.func, self.x, method='L-BFGS-B', callback=self.record)
