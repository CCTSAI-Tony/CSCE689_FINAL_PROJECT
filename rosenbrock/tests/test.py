import pytest
import re
import numpy as np
import scipy.optimize
import time

from rosenbrock.__main__ import print_header
from nelder_mead import NelderMead
from conjugate_gradient import ConjugateGradient
from L_BFGS_B import L_BFGS_B
