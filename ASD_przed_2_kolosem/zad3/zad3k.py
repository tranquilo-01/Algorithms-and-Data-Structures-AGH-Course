from math import inf

from zad3ktesty import runtests


def ksuma(T, k):
    tlen = len(T)
    results = [-1 for _ in range(tlen)]
    for i in range(k):
        results[i] = T[i]

    for i in range(k, tlen):
        minn = inf
        for j in range(i-k, i):
            minn = min(minn, results[j])
        results[i] = minn + T[i]

    return min(results[tlen-k:])


runtests(ksuma)
ksuma([1, 2, 3, 4, 6, 15, 8, 7], 2)