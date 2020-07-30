# Implemented by Python3

## To implement this Software, run the following commands.

### python -m rosenbrock

## To run the test suite, run the following commands.

### pytest

# CSCE 689 SPTP: SFTWR ENG FOR SCI/ENG

## • Introduction

### The purpose of the software is to compare three optimization algorithms and their performances based on Rosenbrock function, and the three algorithms are called Nelder-Mead, Conjugate Gradient and L-BFGS-B.The Rosenbrock function is defined as:

## 𝑓𝑅𝑜𝑠𝑒𝑛(𝑥,𝑦)=(100(𝑦−𝑥2) 2+(1−𝑥) 2

### Once the software being executed, it prints out a table which states how many iterations each algorithm take, and overall runtime respectively.

### It also outputs a plot that includes different results of the three algorithms which all start form point (-3,-4) and terminate at point (1,1) as the minimum location of the Rosenbrock function.

## • Graph

![image](https://github.com/CCTSAI-Tony/CSCE689_FINAL_PROJECT/blob/master/rosenbrock/graph.jpg)

## • Improvement

### Refactor source_code.py into a package project and include its own test suit using PyTest. Be optimized by NumPy/SciPy and overall run time has been improved from 216ms to 13ms (10 times faster).

## • Original result

![image](https://github.com/CCTSAI-Tony/CSCE689_FINAL_PROJECT/blob/master/rosenbrock/source.jpg)

## • Rebuilt result

![image](https://github.com/CCTSAI-Tony/CSCE689_FINAL_PROJECT/blob/master/rosenbrock/package.jpg)
