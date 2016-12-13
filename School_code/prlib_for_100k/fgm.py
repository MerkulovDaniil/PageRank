#Fast Gradient method

import numpy as np

def read(graph):
    n = graph.shape[0]
    for i in range(n):
        graph[i, i] -= 1
    graph = graph.transpose()
    return graph.tocoo().tocsr(), n

def norma(vector):
    return np.linalg.norm(vector, 2)

def f(A, x):
    return 0.5 * np.linalg.norm(A.dot(x)) ** 2

def grad(A, x, b):
    return A.T.dot(A.dot(x) - b)

def f_(xnew, x, L, gradi, A, b):
    return f(A, x, b) + np.dot(gradi, xnew - x) + (L * norma(xnew - x) ** 2 / 2)

def fgm(graph):
    A, n = read(graph)
    x = np.array([0.0] * n)
    x[0] = 1.0
    EPS = 10 ** (-7)
    while f(A, x) > EPS:
        x = A.dot(x) + x
    x = x / x.sum()
    print(*x)
    return x
