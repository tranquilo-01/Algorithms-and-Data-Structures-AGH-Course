# Mamy dana tablice z nominałami monet stosowanych w pewnym dziwnym
# kraju, oraz kwote T. Prosze podac algorytm, który oblicza minimalna ilosc monet potrzebna do wydania
# kwoty T (algorytm zachłanny, wydajacy najpierw najwieksza monete, nie działa: dla monet 1, 5, 8 wyda
# kwote 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).
from math import inf


def change_exp(coins, amount):
    minn = inf
    if amount == 0:
        return 0

    for i in coins:
        if i <= amount:
            result = change_exp(coins, (amount - i)) + 1
            if result < minn:
                minn = result
    return minn


def change_memo(coins, amount):
    lookup = [0 for _ in range(amount + 1)]


    def rec(c, a):
        minn = inf

        if amount == 0:
            return 0

        if lookup[a]:
            return lookup[a]

        for i in range(len(c)):
            if c[i] <= a:
                result = rec(c, (a - c[i])) + 1
                if result < minn:
                    lookup[a] = result
                    minn = result
        return lookup[a]

    r = rec(coins, amount)
    return r


# print(change_exp([2, 3, 5, 7, 4, 12, 17, 29, 47, 79], 43))
print(change_memo([2, 3, 5, 7, 4, 12, 17, 29, 47, 79], 43))
