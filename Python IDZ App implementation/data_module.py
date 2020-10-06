import sympy
import numpy
import math

if __name__ == '__main__':
    print("Module with data for equations")


SIGNS_TO_ROUND = 4
EPS = pow(10, -SIGNS_TO_ROUND)
ITER = 100

#task 1
gauss_matrix = numpy.array([[3.21, -4.25, 2.13, 5.06],
                            [7.09, 1.17, -2.33, 4.75],
                            [0.43, -1.42, -0.62, 1.05]])
#task 2
gauss_iter_matrix = numpy.array([[-0.77, -0.04, 0.21, -0.18, -1.24],
                                 [0.45, 1.23, 0.06, 0, 0.88],
                                 [0.26, 0.34, -1.11, 0, -0.62],
                                 [0.05, -0.26, 0.34, -1.12, 1.17]])
#task 3
gauss_zeidel_matrix = numpy.array([[2.7, 3.3, 1.3, 2.1],
                            [3.5, -1.7, 2.8, 1.7],
                            [4.1, 5.8, -1.7, 0.8]])
#task 4
gauss_det_matrix = numpy.array([[1, 0.17, -0.25, 0.54],
                         [0.42, 1, 0.67, -0.32],
                         [-0.11, 0.35, 1, -0.74],
                         [0.55, 0.43, 0.36, 1]])
#task 5
matrix_for_inverse = numpy.array([[1, 0.421, 0.54, 0.66],
                                  [0.42, 1, 0.32, 0.44],
                                  [0.54, 0.32, 1, 0.22],
                                  [0.66, 0.44, 0.22, 1]])


#task 6, 7
def func6_7(x):
    return math.e ** x + x


#task 6, 7
def dfunc6_7(x):
    #x_ = sympy.Symbol('x')
    #func = math.e ** x_ + x_
    #func_deriv = sympy.diff(func)
    #print("function: ", func)
    #print("derivative: ", func_deriv)
    return math.e**x + 1


#task8
krylov = numpy.array([[1, -1, 2],
                      [1, 2, 1],
                      [2, 0, 3]])

#task9
polynom_points = (numpy.array([0, 1, 2, 3, 4]), numpy.array([1, 4, 40, 15, 85]))


#task10
def func10(x):
    return math.sqrt(1 + x**4)


task10tuple = (func10, 0, 1)

#task11
a, b = 2.1, 1.8
A, B = 1.7, 0.5
n = 10


def p(x):
    return 0.8


def q(x):
    return -x


def f(x):
    return 1.4


task11tuple = (a, b, A, B, n, p, q, f)
