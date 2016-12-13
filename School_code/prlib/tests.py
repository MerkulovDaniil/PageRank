from finished_bo import bak_ost
from fgm import fgm
import math
import numpy as np
import time

def clog(x):
    vector = list(sorted(x, reverse=True))
    k = [math.log2(i) for i in range(1, len(vector) + 1)]
    ln = len(vector)
    y = [math.log2(i) for i in vector]
    A = np.vstack([k, np.ones(len(k))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    return m

def main():
    result = open("test_res2.txt", "w")
    a_variants = [0.5, 0.25, 0.75, 0.3]
    for a in a_variants:
        result.write(str(a) + "\n")
        print(a)
        for k in range(5):
            graph = bak_ost(100000, 10, a)
            t = time.time()
            x = fgm(graph)
            t  = time.time() - t
            lg = clog(x)
            print(lg, t)
            result.write(str(lg) + " " + str(t) + "\n")
            graph = 0
    result.close()

main()
