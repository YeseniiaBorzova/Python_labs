import numpy


def gauss_solve(A):
    a = A[:, :-1]
    b = A[:, -1]
    n = b.size
    x = numpy.zeros(n)

    for k in range(n - 1):
        for i in range(k + 1, n):
            c = -a[i, k] / a[k, k]
            a[i, k] = 0
            a[i, k + 1:n] += c * a[k, k + 1:n]
            b[i] += c * b[k]
            #print('k: ', c)
            #print('matrix :\n', a)
            #print('b matrix: ', b)

    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 1, -1, -1):
        s = sum(a[i, i + 1:n] * x[i + 1:n])
        x[i] = (b[i] - s) / a[i, i]
        #print('x: ({} - {}) / {}'.format(b[i], s, a[i, i]))

    return x


def gauss_iteration(A, eps):
    a = A[:, :-1]
    b = A[:, -1]
    x0 = numpy.zeros(len(a))

    D = numpy.diag(a)
    R = a - numpy.diagflat(D)

    #by count of iterations
    #for _ in range(iter):
    #    x = (b - numpy.dot(R, x)) / D
    #    print(x)

    def util():
        x = (b - numpy.dot(R, x0)) / D
        #[print('\t({} - {}) / {} = {}'.format(b_, dot_, d_, x_))
        # for b_, dot_, d_, x_ in
        # zip(b, numpy.dot(R, x), D, x)]
        #print(x)
        return x

    x = util()
    while eps <= numpy.all(x.round(4) - x0.round(4)):
        x0 = x[:]
        x = util()

    return x


def gauss_zeidel(a):
    a = numpy.array(a)

    len1 = len(a[:, 0])
    len2 = len(a[0, :])

    for i in range(len1):
        main_elem = numpy.diag(a)
        a[i, i:len2] /= main_elem[i]
        for j in range(i+1, len1):
            a[j, i:len2] -= a[i, i:len2]*a[j, i]

    for i in reversed(range(1, len1)):
        for j in reversed(range(i)):
            a[j, len1] -= a[j, i] * a[i, len1]

    return a[:, len2 - 1]


def gauss_det(a):
    res = 1
    n = len(a)
    D = numpy.diag(a)
    if 0 in D:
        return 0

    for i in range(n):
        j = max(range(i, n), key=lambda k: abs(a[k, i]))
        if i != j:
            a[i], a[j] = a[j], a[i]
            res *= -1
        res *= D[i]
        for j in range(i + 1, n):
            b = a[j, i] / D[i]
            a[j] = [a[j, k] - b * a[i, k] for k in range(n)]
            #print('k: ', b.round(4))
            #print('a: \n', a.round(4))
    return res


def gauss_inverse(a):
    n = len(a)
    res = numpy.eye(n)
    a_big = numpy.zeros((n, 2*n))

    a_big[:, :n] = a[::]
    a_big[:, n:2*n] = res[::]

    for k in range(n):
        a_big[:, :2*n] /= a[k, k]
        for i in range(k+1, n):
            K = a_big[i, k] / a_big[k, k]
            a_big[i, :2*n] -= a_big[k, :2*n] * K
        #print(a_big.round(4))
        a[::] = a_big[:, :n]

    for k in reversed(range(n)):
        for i in reversed(range(2 * n)):
            a_big[k, i] /= a[k, k]

        for i in reversed(range(k)):
            K = a_big[i, k] / a_big[k, k]
            for j in reversed(range(2 * n)):
                a_big[i, j] -= a_big[k, j] * K
            #print(a_big.round(4))
    #print(a_big.round(4))
    res[::] = a_big[:, n:2*n]
    return res


if __name__ == '__main__':
    print("This module contains all implemented functions to solve matrix equations")
    print("Gauss solution: ", gauss_solve.__name__)
    print("Gauss-Zeidel solution: ", gauss_zeidel.__name__)
    print("Gauss iterative method: ", gauss_iteration.__name__)
    print("Det by Gauss: ", gauss_det.__name__)
    print("Inverse matrix by Gauss: ", gauss_inverse.__name__)

