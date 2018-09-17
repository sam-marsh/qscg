import numpy as np
from qscg import *


def random_f(n, d):
    N = 2**n
    m = np.random.random_integers(0, 1, size=(N, N))
    m = np.tril(m) + np.tril(m, -1).T
    for x in range(N):
        while sum(m[x]) > d:
            r = np.random.randint(0, N)
            while m[x, r % N] == 0:
                r = r + 1
            m[x, r % N] = 0
            m[r % N, x] = 0

    print(m)
    print("----")

    def f(x, i):
        k = 0
        count = 0
        while k < N:
            if m[x, k] != 0:
                if count == i:
                    return k, m[x, k]
                count = count + 1
            k = k + 1
        return x, 0

    return f


if __name__ == '__main__':
    n = 3
    d = 4
    md = OneSparseDecomposer(random_f(n, d), d, n)  # lambda x, i: (x ^ (1 << i), 1), n, n)
    # md.display_matrix()

    ms = [[[np.zeros((2**n, 2**n)).astype(int) for _ in range(6)] for _ in range(d)] for _ in range(d)]

    for x in range(2**n):
        for i in range(d):
            for j in range(d):
                for uid in range(6):
                    y, h = md.g(x, i, j, uid)
                    ms[i][j][uid][x][y] = h

    ms = [item for sublist in ms for item in sublist]
    ms = [item for sublist in ms for item in sublist]

    for m in ms:
        if not np.array_equal(m, np.zeros((2**n, 2**n)).astype(int)):
            print(m)

    # print(np.sum(ms, axis=0))
