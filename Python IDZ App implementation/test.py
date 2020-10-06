from numpy import linalg
from scipy.optimize import newton
from scipy import integrate
from scipy.interpolate import lagrange
from data_module import *
from matrix_module import *
from function_module import *


print('task1')
print('numpy solution: ', linalg.solve(gauss_matrix[:, :-1], gauss_matrix[:, -1]).round(SIGNS_TO_ROUND))
print("gauss solution: ", gauss_solve(gauss_matrix).round(SIGNS_TO_ROUND))

print('\ntask2')
print('numpy solution: ', linalg.solve(gauss_iter_matrix[:, :-1], gauss_iter_matrix[:, -1]).round(SIGNS_TO_ROUND))
print('gauss iteration: ', gauss_iteration(gauss_iter_matrix, EPS).round(SIGNS_TO_ROUND))

print('\ntask3')
print('numpy solution: ', linalg.solve(gauss_zeidel_matrix[:, :-1], gauss_zeidel_matrix[:, -1]).round(SIGNS_TO_ROUND))
print("gauss-zeidel solution: ", gauss_zeidel(gauss_zeidel_matrix).round(SIGNS_TO_ROUND))

print('\ntask4')
print('numpy det: ', linalg.det(gauss_det_matrix).round(SIGNS_TO_ROUND))
print('gauss det: ', gauss_det(gauss_det_matrix).round(SIGNS_TO_ROUND))

print('\ntask5')
print('numpy inverse: \n', linalg.inv(matrix_for_inverse).round(SIGNS_TO_ROUND))
print('gauss inverse: \n', gauss_inverse(matrix_for_inverse).round(SIGNS_TO_ROUND))

print('\ntask6')
print('scipy newton solution: ', newton(func6_7, 1).__round__(SIGNS_TO_ROUND))
print('newton solution: ', newtons_method(func6_7, dfunc6_7, 1, EPS).__round__(SIGNS_TO_ROUND))

print('\ntask7')
print('scipy newton solution: ', newton(func6_7, 1).__round__(SIGNS_TO_ROUND))
print('simple iteration method: ', simple_iter_method(func6_7, dfunc6_7, 1, EPS).__round__(SIGNS_TO_ROUND))

print('\ntask8')
print('scipy krylov solution: \ncoeffitients: {}\nmatrix\n{}'.format(linalg.eig(krylov)[0], linalg.eig(krylov)[1]))

print('\ntask9')
print('lagrange and newton polynomial: \n', lagrange(*polynom_points))

print('\ntask10')
print('scipy solution: ', integrate.quad(*task10tuple)[0].__round__(SIGNS_TO_ROUND))
print('trapeze method: ', trapeze_method(*task10tuple, EPS).__round__(SIGNS_TO_ROUND))
print('simpson method: ', simpson_method(*task10tuple, EPS).__round__(SIGNS_TO_ROUND))

print('\ntask11')
print(task11func(*task11tuple))
