import numpy as np
import time
from scipy.sparse import csr_matrix

prograph = open('probability graph.txt')
data = open("inbox", "w")

def read(graph):  # matrix reading
    global n
    n = int(graph.readline())  # n - length
    data = [[] for i in range(n)]
    for i in range(n):
        data[i] = list(map(float, graph.readline().split()))
        data[i][i] -= 1
    data = np.array(data)
    data = data.T
    data = csr_matrix(data)
    return data

def f(x):  # f(x) - permanent function
    return 0.5 * np.linalg.norm(A.dot(x)) ** 2

def main():
    global A, n, x, b
    A = read(prograph)  # probability graph (matrix)
    prograph.close()
    x = np.array([0.0] * n)  # PageRank vector
    x[0] = 1.0
    EPS = 10 ** -7  # accuracy
    firstage = time.time()
    while f(x) > EPS:
        x = A.dot(x) + x
    x /= x.sum()
    print(f(x))
    print(time.time() - firstage)
    data.write(" ".join(map(str, x)))

main()
