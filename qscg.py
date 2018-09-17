import numpy as np
import scipy as sp


def bit_get(x, i):
    return (x >> i) & 1


class Decomposer:
    pass


class OneSparseDecomposer:
    """
    https://arxiv.org/pdf/quant-ph/0508139.pdf
    """

    def __init__(self, f, d, n):
        self.f = f
        self.d = d
        self.n = n
        self.N = 2 ** n

    def zn(self):
        l = 2 ** self.n
        zn = 0
        while l > 6:
            l = 2 * np.ceil(np.log2(l)).astype(int)
            zn = zn + 1
        return zn

    def _seq0(self, x, i, j):
        zn = self.zn()
        seq = [x]
        while len(seq) <= zn + 1:
            x = seq[-1]
            xn = self.f(x, i)[0]
            if x < xn:
                seq.append(xn)
            else:
                break
        return seq

    def _seq1(self, seq0, bits):
        idx_len = np.ceil(np.log2(bits)).astype(int)
        seq1 = []
        for x, xn in zip(seq0, seq0[1:]):
            c = bits - 1
            while bit_get(x, c) == bit_get(xn, c):
                c = c - 1
            diff_bit = bits - c - 1
            seq1.append((bit_get(x, c) << idx_len) | diff_bit)
        seq1.append(bit_get(seq0[-1], bits - 1) << idx_len)
        return seq1, idx_len + 1

    def get_j(self, x, y):
        for j in range(self.d):
            if self.f(y, j)[0] == x:
                return j

    def get_uid(self, x, i, j):
        seq = self._seq0(x, i, j)
        idx = self.n
        for i in range(self.zn()):
            seq, idx = self._seq1(seq, idx)
        return seq[0]

    def display_matrix(self):
        m = [['(x, x, x)'] * self.N for _ in range(self.N)]
        for x in range(self.N):
            for i in range(self.d):
                y = self.f(x, i)[0]
                j = self.get_j(x, y)
                m[x][y] = str((i, j, self.get_uid(x, i, j))) if x < y else str((j, i, self.get_uid(x, i, j)))
        for x in m:
            print('\t'.join(x))

    def g(self, x, i, j, uid):
        if self.f(x, i)[0] == x and i == j and uid == 0:
            return self.f(x, i)
        if self.f(x, i)[0] > x and self.f(self.f(x, i)[0], j)[0] == x and self.get_uid(x, i, j) == uid:
            return self.f(x, i)
        if self.f(x, j)[0] < x and self.f(self.f(x, j)[0], i)[0] == x and self.get_uid(self.f(x, j)[0], i, j) == uid:
            return self.f(x, j)
        return x, 0

    def _lt2(self, hs, m, l):
        return np.product(
            sp.linalg.expm(hs[i] * l / 2) * np.product(sp.linalg.expm(hs[j] * l / 2) for j in range(m, step=-1))
            for i in range(m))

    def lt(self, hs, m, l, k):
        if k == 2:
            return self._lt2(hs, m, l)
        pk = np.power(4 - np.power(4, 1.0 / (2 * k - 1)), -1)
        return np.power(self.lt(hs, m, pk * l, 2 * k - 2), 2) * np

    def compute_unique_index(self, x, i, j):
        pass
