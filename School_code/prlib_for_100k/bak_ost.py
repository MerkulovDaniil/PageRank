from random import randint as rnd
from scipy.sparse import dok_matrix

def bak_ost(V, K, a):
    graph = dok_matrix((V // K, V // K))
    numbers = [0] * (V // K)
    graph[0, 0] = 1
    vertexs = [0, 0] + (a - 1) * [0]
    for i in range(1, V):
        f = rnd(1, (a + 1) * (i + 1) - 1)
        if f <= a:
            j = i
        else:
            j = vertexs[rnd(0, len(vertexs) - 1)]
        vertexs.append(j)
        vertexs.append(i)
        graph[j // K, i // K] += 1
        graph[i // K, j // K] += 1
        numbers[j // K] += 1
        numbers[i // K] += 1
        vertexs += (a - 1) * [i]
    for i in graph.keys():
        graph[i[0], i[1]] /= numbers[i[0]]
    return graph