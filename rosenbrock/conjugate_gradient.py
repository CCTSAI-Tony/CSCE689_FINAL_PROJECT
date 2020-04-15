import scipy.optimize
from rosenbrock.nelder_mead import NelderMead


class ConjugateGradient(NelderMead):


    def optimize(self):
        self.res = scipy.optimize.minimize(self.func, self.x, method='CG', callback=self.record)
