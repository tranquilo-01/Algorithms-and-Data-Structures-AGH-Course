from math import inf
from zad4ktesty import runtests


def falisz(T):
    tlen = len(T)
    lookup = [[-1 for _ in range(tlen)] for _ in range(tlen)]

    def rek(a, b):

        if lookup[a][b] != -1:
            return lookup[a][b]

        if a < 0 or b < 0:
            return inf

        if a == 0 and b == 0:
            return 0

        lookup[a][b] = min(rek(a-1, b) + T[a][b], rek(a, b-1) + T[a][b])
        return lookup[a][b]

    return rek(tlen-1, tlen-1)


runtests(falisz)
