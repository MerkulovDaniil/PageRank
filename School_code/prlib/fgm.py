#Fast Gradient method

import numpy as np
import time
from scipy.sparse import csr_matrix

EPS = 10 ** -7

def read(graph):
    ti = time.time()
    n = graph.shape[0]
    for i in range(n):
        graph[i, i] -= 1
    graph = graph.tocsr().T.todok()
    graph.resize((n + 1, n))
    for i in range(n):
        graph[n, i] = 1.0 / n
    return graph.tocsr(), n

def powerread(graph):  # matrix reading
    n = graph.shape[0]
    for i in range(n):
        graph[i, i] -= 1
    graph = graph.tocsr().T
    return graph, n

def norma(vector):
    return np.linalg.norm(vector, 2)

def f(A, x, b):
    return 0.5 * norma(A.dot(x) - b) ** 2

def grad(A, x, b):
    return A.T.dot(A.dot(x) - b)

def f_(xnew, x, L, gradi, A, b):
    return f(A, x, b) + np.dot(gradi, xnew - x) + (L * norma(xnew - x) ** 2 / 2)

def fgm(graph):
    A, n = read(graph)
    k = 0
    b = np.array([0] * (n + 1))
    b[-1] = 1 / n
    x = np.array([0] * n)
    x[0] = 1.0
    L = 10
    z = x.copy()
    ynew = (2 * z + k * x) / (k + 2)
    grady = grad(A, ynew, b)
    xnew = ynew - grady / L
    znew = z - (k + 2) * grady / (2 * L)
    k += 1
    while f(A, x, b) > EPS:
        while f_(xnew, ynew, L, grady, A, b) < f(A, xnew, b):
            L *= 2
            grady = grad(A, ynew, b)
            xnew = ynew - grady / L
            znew = z - (k + 2) * grady / (2 * L)
        x, y, z = xnew, ynew, znew
        grady = grad(A, ynew, b)
        L /= 2
        k += 1
        ynew = (2 * z + k * x) / (k + 2)
        xnew = ynew - grady / L
        znew = z - (k + 2) * grady / (2 * L)
    x = x / x.sum()
    x += abs(min(x)) + 1
    return x


def powerm(graph):
    A, n = powerread(graph)  # probability graph (matrix)
    x = np.array([0.0] * n)  # PageRank vector
    x[0] = 1.0
    b = np.array([0] * (n))
    while f(A, x, b) > EPS:
        x = A.dot(x) + x
    x /= x.sum()
    return x

def gamma(k):
    return 2 / (k + 2)

""" work in progress
def conditionalGM(graph):
    global D, A, n, z, b
    A = read(graph)  # probability graph (matrix)
    z = np.array([0.0] * n)  # PageRank vector
    z[0] = 1.0
    EPS = 10 ** (-4)  # accuracy\
    print(1)
    beta = 1
    AdotAT = A.T.dot(A)
    D = AdotAT.dot(z)
    AdotAT = AdotAT.toarray()
    firstage = time.time()
    print(10 * EPS ** (-1))

    # for k in range(1, int(EPS ** (-1))):
    k = 1
    y = np.array([0.0 for i in range(n)])
    iold = 0
    while k % 1000 != 0 or f(beta * z) > EPS:
        ti = time.time()
        i = np.argmin(D)
        y[iold] = 0.0
        y[i] = 1.0
        sig = (gamma(k) / beta)
        z[i] += sig
        D += sig * AdotAT[:, i]
        beta *= (1 - gamma(k + 1))
        k += 1
        iold = i
        print(time.time() - ti)
    print(f(beta * z))
    print(time.time() - firstage)
"""
