import numpy as np
import time
from scipy.sparse import csr_matrix
from random import randint as rnd
import math

V = 100000
K = 10
a = 50
EPS = 10 ** -7

def rand(n):
    f = rnd(1, (a + 1) * (n + 1) - 1)
    if f <= a:
        return(n)
    else:
        return(vertexs[rnd(0, len(vertexs) - 1)])

def edge(j, i):
    global vertexs
    vertexs.append(j)
    vertexs.append(i)
    graph[j // K][i // K] += 1
    graph[i // K][j // K] += 1
    numbers[j // K] += 1
    numbers[i // K] += 1
    vertexs += (a - 1) * [i]

def main():
    global vertexs, graph, numbers
    starttime = time.time()
    graph = [[0] * (V // K) for i in range(V // K)]
    numbers = [0] * (V // K)
    graph[0][0] = 2
    vertexs = [0, 0] + (a - 1) * [0]
    for i in range(1, V):
        j = rand(i)
        edge(j, i)
    for i in range(V // K):
        for j in range(V // K):
            graph[i][j] /= numbers[i]
    #print(time.time() - starttime)


def read(graph):  # matrix reading
    global n
    n = V // K  # n - length
    data = graph
    for i in range(n):
        data[i][i] -= 1
    data = np.array(data)
    data = data.T
    data = csr_matrix(data)
    return data

def f(x):  # f(x) - permanent function
    return 0.5 * np.linalg.norm(A.dot(x)) ** 2

def main2():
    global A, n, x, b
    A = read(graph)  # probability graph (matrix)
    x = np.array([0.0] * n)  # PageRank vector
    x[0] = 1.0
    firstage = time.time()
    while f(x) > EPS:
        x = A.dot(x) + x
    x /= x.sum()
    #print(f(x))
    #print(time.time() - firstage)

def main3():
    global x
    vector = sorted(x, reverse=True)
    x = [math.log2(i) for i in range(1, len(vector) + 1)]
    y = [math.log2(i) for i in vector]
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    print(m)

for i in range(10):
    main()
    main2()
    main3()
