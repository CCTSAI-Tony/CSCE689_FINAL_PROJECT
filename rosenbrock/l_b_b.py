import scipy.optimize
from rosenbrock.nelder_mead import NelderMead


class L_BFGS_B(NelderMead):


    def optimize(self):
        self.res = scipy.optimize.minimize(self.func, self.x, method='L-BFGS-B', callback=self.record)
