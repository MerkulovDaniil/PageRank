import numpy as np
import time
from heapq import *
from scipy.sparse import csr_matrix

starttime = time.time()
prograph = open('probability graph.txt')

def read(graph):  # matrix reading
    global n
    n = int(graph.readline())  # n - length
    data = [[] for i in range(n)]
    for i in range(n):
        data[i] = list(map(float, graph.readline().split()))
        data[i][i] -= 1
    data = np.array(data)
    data = data.T
    #ones = np.array([1 / n] * n)
    #data = np.row_stack((data, ones))
    data = csr_matrix(data)
    return data

def norma(vector):  # 2-norma
    return np.linalg.norm(vector, 2)

def f(x):  # f(x) - permanent function
    return 0.5 * norma(A.dot(x)) ** 2

def grad(x):  # return gradient of f(x) = 0.5 * norma(A * x) ** 2
    return A.T.dot(A.dot(x))

def gamma(k):
    return 2 / (k + 2)

def main():
    global D, A, n, z, b
    A = read(prograph)  # probability graph (matrix)
    prograph.close()
    z = np.array([0.0] * n)  # PageRank vector
    z[0] = 1.0
    EPS = 10 ** (-4)  # accuracy
    beta = 1
    D = np.array(grad(z))
    AdotAT = A.T.dot(A).toarray()
    firstage = time.time()
    k = 1
    y = np.array([0.0 for i in range(n)])
    iold = 0
    while k % 1000 != 0 or f(beta * z) > EPS:
        i = np.argmin(D)
        y[iold] = 0.0
        y[i] = 1.0
        sig = (gamma(k) / beta)
        z[i] += sig
        D += sig * AdotAT[:, i]
        beta *= (1 - gamma(k + 1))
        k += 1
        iold = i
    print(f(beta * z))
    print(time.time() - firstage)

main()
