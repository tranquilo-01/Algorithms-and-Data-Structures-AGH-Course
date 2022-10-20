# - miasta to punkty w R^2 (zadne 2 nie maja tego samego x)
# - miasto 0 ma najmniejsze x
# - trasa przechodzi z lewa na prawo i z powrotem (zmiana kierunku tylko raz)
# opis wyklad 7

from math import inf


def d(i, j):
    return ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** (1 / 2)


def outside(tab, i, j):
    n = len(tab)
    F = [[inf for j in range(n)] for i in range(n)]  # przechowujemy wartosci funkcji f(i, j)
    D = [[-1 for j in range(n)] for i in range(n)] # przechowujwmy dystanse miedzy punktami
    for i in range(n):
        for j in range(n):
            D[i][j] = d(tab[i], tab[j])

    def tspf(i, j):
        if F[i][j] != inf:
            return F[i][j]
        if i == j - 1:
            best = inf
            for k in range(j-1):
                best = min(best, tspf(k, j-1) + D[k][j])
            F[j-1][j] = best
        else:
            F[i][j] = tspf(i, j-1) + D[j-1][j]
        return F[i][j]

    return tspf(i, j)



