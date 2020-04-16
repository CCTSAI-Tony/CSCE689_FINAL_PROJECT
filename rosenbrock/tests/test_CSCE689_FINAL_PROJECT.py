import pytest
import re
import numpy as np
import scipy.optimize
import time

from rosenbrock.rosenbrock import rosenbrock
from rosenbrock.nelder_mead import NelderMead
from rosenbrock.conjugate_gradient import ConjugateGradient
from rosenbrock.l_b_b import L_BFGS_B
from rosenbrock.tests.nelder_mead_array import *
from rosenbrock.tests.conjugate_gradient_array import *
from rosenbrock.tests.l_b_b_array import *
from rosenbrock.__main__ import print_result

nel_md_test = NelderMead(rosenbrock, [(-3, -4)])
cg_test = ConjugateGradient(rosenbrock, [(-3, -4)])
lbb_test = L_BFGS_B(rosenbrock, [(-3, -4)])

def test_rosenbrock():

    case1 = (1,1)
    case2 = (3,4)
    case3 = (5,8)
    case1_result = rosenbrock(case1)
    case2_result = rosenbrock(case2)
    case3_result = rosenbrock(case3)
    assert(np.allclose(case1_result,0))
    assert(np.allclose(case2_result,2504))
    assert(np.allclose(case3_result,28916))


def test_NelderMead():
    '''
    from nelder_mead_array imprt array1, confirm it is the correct np.array
    '''

    nel_md_iteration = nel_md_test.iteration
    assert(np.allclose(nel_md_iteration,75))
    nel_md_array = nel_md_test.x
    assert(np.allclose(nel_md_array, array1))


def test_ConjugateGradient():
    '''
    from nelder_mead_array imprt array2, confirm it is the correct np.array
    '''

    cg_iteration = cg_test.iteration
    assert(np.allclose(cg_iteration,37))
    cg_array = cg_test.x
    assert(np.allclose(cg_array, array2))

def test_L_BFGS_B():
    '''
    from nelder_mead_array imprt array3, confirm it is the correct np.array
    '''

    lbb_iteration = lbb_test.iteration
    assert(np.allclose(lbb_iteration,29))
    lbb_array = lbb_test.x
    assert(np.allclose(lbb_array, array3))


def test_print_result(capsys):
    print_result(nel_md_test, cg_test, lbb_test)
    captured_output = capsys.readouterr()
    output_lines = captured_output.out.splitlines()
    nel_md_pattern = re.compile(".*\\s*Nelder-Mead.*75.*\\d+.*")
    cg_pattern = re.compile(".*\\s*Conjugate Gradient.*37.*\\d+.*")
    lbb_pattern = re.compile(".*\\s*L-BFGS-B.*29.*\\d+.*")
    assert(output_lines[0] == "Frank's Optimization Research")
    assert(output_lines[1] == "| Method             | Iterations | Time (ms) |")
    assert(output_lines[2] == "+--------------------+------------+-----------+")
    assert(nel_md_pattern.fullmatch(output_lines[3]) != None)
    assert(cg_pattern.fullmatch(output_lines[4]) != None)
    assert(lbb_pattern.fullmatch(output_lines[5]) != None)
