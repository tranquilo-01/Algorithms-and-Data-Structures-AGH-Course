# Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Nalezy przejsc z pola (1, 1) na pole (n,n) korzystajac jedynie z ruchów “w dół”
# oraz “w prawo”. Wejscie na dane pole kosztuje tyle, co znajdujaca sie tam liczba. Prosze podac algorytm
# znajdujacy trase o minimalnym koszcie
from math import inf


def walk_exp(cost, i, j):
    if j < 0 or i < 0:
        return inf
    if i == 0 and j == 0:
        return cost[i][j]
    else:
        return cost[i][j] + min(walk_exp(cost, i - 1, j), walk_exp(cost, i, j - 1))


def walk_memo(cost):
    i = j = len(cost) - 1
    lookup = [[-1 for _ in range(j + 1)] for _ in range(j + 1)]
    lookup[0][0] = cost[0][0]

    def rec(i, j):
        if j < 0 or i < 0:
            return inf

        if lookup[i][j] != -1:
            return lookup[i][j]

        lookup[i][j] = cost[i][j] + min(rec(i - 1, j), rec(i, j - 1))
        return lookup[i][j]

    r = rec(i, j)
    # for row in lookup:
    #     print(row)
    return r



arr = [[3, 4, 7],
       [1, 40, 9],
       [7, 6, 12]]

print(walk_exp(arr, 2, 2))
print(walk_memo(arr))

