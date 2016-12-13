from random import randint as rnd
import time

matrix = open('probability graph.txt', 'w')
#data = open("inbox_data", "w")

V = 10000
K = 10
a = 9

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
    #graph[i // K][j // K] += 1
    #inbox[j // K].append(i // K)
    #inbox[i // K].append(j // K)
    numbers[j // K] += 1
    #numbers[i // K] += 1
    vertexs += (a - 1) * [i]


def for_print():
    matrix.write(str(V // K))
    matrix.write("\n")
    #data.write(str(V // K))
    #data.write("\n")
    for i in range(V // K):
        matrix.write(" ".join(map(str, graph[i])))
        matrix.write("\n")
        #data.write(" ".join(map(str, inbox[i])))
        #data.write("\n")

def division():
    for i in range(V // K):
        for j in range(V // K):
            graph[i][j] /= numbers[i]

def main():
    global vertexs, graph, numbers#, inbox
    starttime = time.time()
    graph = [[0] * (V // K) for i in range(V // K)]
    numbers = [0] * (V // K)
    graph[0][0] = 1
    vertexs = [0, 0] + (a - 1) * [0]
    #inbox = [[] for i in range(V // K)]
    for i in range(1, V):
        j = rand(i)
        edge(j, i)
    division()
    for_print()
    print(time.time() - starttime)

main()
