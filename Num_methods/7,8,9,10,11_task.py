import numpy as np
from scipy.interpolate import lagrange
from numpy import linalg
import math
def newton7(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None
p = lambda x: math.e**(-x)-math.log(x,math.e)
Dp = lambda x: -1*math.e**(-x)-(1/x)
approx = newton7(p,Dp,1,1e-10,10)
print("(7)_Root by Newtom method - ",approx)


krylov = np.array([[3,1,1],
                  [1,2,3],
                  [-2,5,-2]])
print("(8)_Compute the eigenvalues \n",linalg.eig(krylov)[0]," \n Right eigenvectors of a square array \n",linalg.eig(krylov)[1])



lagr_x=np.array([1,3,5,7,9])
lagr_y=np.array([0.5,2,7.5,20,42.5])
print("(9)_Lagrange interpolation \n",lagrange(lagr_x,lagr_y))
def getNDDCoeffs(x, y):
    n = np.shape(y)[0]
    pyramid = np.zeros([n, n])
    pyramid[::,0] = y
    for j in range(1,n):
        for i in range(n-j):
            pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid[0]
coeff_vector = getNDDCoeffs(lagr_x, lagr_y)
final_pol = np.polynomial.Polynomial([0.])
n = coeff_vector.shape[0]
for i in range(n):
    p = np.polynomial.Polynomial([1.])
    for j in range(i):
        p_temp = np.polynomial.Polynomial([-lagr_x[j], 1.])
        p = np.polymul(p, p_temp)
    p *= coeff_vector[i]
    final_pol = np.polyadd(final_pol, p)
p = np.flip(final_pol[0].coef, axis=0)
print("(9)_Newton interpolation coeffs: \n",p)


def f10(x):
    return math.sqrt(1+x*x*x)
a,b,n=0,3,10
def Trapezoidal(f, a, b, n):
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))
    for i in range(1,n,1):
        s = s + f(a + i*h)
    return h*s
def simpson(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,int(n/2) + 1):
        k += 4*f(x)
        x += 2*h
    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)
print("(10)_Trapezoid method -",Trapezoidal(f10,a,b,n),'\n')
print("(10)_Simpson`s method -",simpson(f10,a,b,n),'\n')


def p(x):
    return 2/x
def q(x):
    return -3
def f(x):
    return 2
a,b=1.1,0.8
A,B=3,1.5
n=10
def Problem11(a, b, A, B, n, p, q, f):
    h = (b - a) / n
    D0, D1 = A + h, h
    y = [[A, D0], [0, D1]]
    x = np.arange(a, b + h, h).round(3)

    def get_c1():
        return (B - y[0][-1]) / y[1][-1]

    def get_solv_y_i(i):
        return y[0][i] + get_c1() * y[1][i]

    def div(a, b):
        return a / b

    for i in range(1, n):
        y[0].append(
            div(
                (h ** 2 * f(x[i]) - (1.0 - (h / 2) * p(x[i])) * y[0][i - 1] - (h ** 2 * q(x[i]) - 2) * y[0][i]),
                1 + h / 2 * p(x[i])
            )
        )
        y[1].append(
            div(
                -(1 - h / 2 * p(x[i])) * y[1][i - 1] - (h ** 2 * q(x[i]) - 2) * y[1][i],
                1 + h / 2 * p(x[i])
            )
        )

    solution = [get_solv_y_i(i) for i in range(n + 1)]
    [print('{y_0:4f}\t{y_1:4f}\t{x_:4f}\t{y_:4f}'.
           format(y_0=y0, y_1=y1, x_=x_, y_=y_))
     for y0, y1, x_, y_ in zip(y[0], y[1], x, solution)]

    return x, solution
x, solution = Problem11(a,b,A,B,n,p,q,f);

print("11_Problem x \n",x," \ny \n",solution)

