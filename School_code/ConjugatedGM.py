import numpy as np
import time
from scipy.sparse import csr_matrix
from scipy.optimize import fmin_cg
from scipy.optimize import fmin_bfgs

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
    ones = np.array([1 / n] * n)
    data = np.row_stack((data, ones))
    data = csr_matrix(data)
    return data

def norma(vector):  # 2-norma
    return np.linalg.norm(vector, 2)

def f(x):  # f(x) - permanent function
    return 0.5 * norma(A.dot(x) - b) ** 2

def grad(x):  # return gradient of f(x) = 0.5 * norma(A * x) ** 2
    return A.T.dot(A.dot(x) - b)

def main():
    global A, n, x, b
    A = read(prograph)  # probability graph (matrix)
    prograph.close()
    b = np.array([0] * (n + 1))
    b[-1] = 1.0
    b = b / n
    x = np.array([0] * n)                 #PageRank vector
    x[0] = 1.0
    era = time.time()
    #print(fmin_bfgs(f, x, grad).sum())
    print(fmin_cg(f, x, grad).sum())
    print(time.time() - era)

main()
