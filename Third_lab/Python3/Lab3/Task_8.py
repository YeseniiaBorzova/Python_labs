import numpy as np
import scipy.stats


def matrix_normal_logpdf(X, m, U, V):
    return scipy.stats.matrix_normal.logpdf\
        (X, mean=m, rowcov=U, colcov=V).round(3)


m = np.random.uniform(-1, 1, size=5 * 4). \
    reshape(5, 4).round(3)
U = np.diag([x for x in range(1, 5 + 1)]).round(3)
V = 0.3 * np.identity(4).round(3)
X = m + 0.1

print("\n Mean:\n",m)
print("\n Row covariations:\n",U)
print("\n Column covariations:\n",V)
print("\n Points:\n",X)

print("\nLogariphm of dencity of distribution: ",matrix_normal_logpdf(X, m, U, V))