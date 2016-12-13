import matplotlib.pyplot as plt
import math
import numpy as np
data = open("x15.txt")

def read():
    vector = [[] for i in range(20)]
    for i in range(20):
        s = 0
        for j in range(10):
            s += (float(data.readline()))
        vector[i] = s / 10
    return vector


def main():
    """
    x = [math.log2(i) for i in range(1, len(vector) + 1)]
    y = [math.log2(i) for i in vector]
    plt.subplot(211)
    plt.plot(x, y, label='unsorted')
    plt.legend()
    plt.title('Power law')

    x = [math.log2(i) for i in range(1, len(vector2) + 1)]
    y = [math.log2(i) for i in vector2]
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    print(m, c)
    plt.subplot(212)
    plt.plot(x, y, color='red', label='sorted')
    plt.legend()
    plt.xlabel('Vertex number')
    plt.ylabel('Vertex power')
    plt.grid(True)
    plt.show()"""

    x = sorted(read())
    y = [0, 1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1000, 2000, 3000, 5000]
    plt.subplot(211)
    plt.plot(y[:7], x[:7])
    plt.ylabel('Q')
    plt.grid(True)
    plt.subplot(212)
    plt.plot(y[3:], x[3:])
    plt.xlabel('A')
    plt.ylabel('Q')
    plt.grid(True)
    plt.show()

main()
