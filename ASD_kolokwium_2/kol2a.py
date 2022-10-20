from kol2atesty import runtests
from math import inf
from collections import deque

# algorytm O(nlogn)
# sortujemy tablicę wejsciową
# wspolrzedne kolejnych punktow przesiadkowych zapisujemy w tablicy przesiadkowe
# nastepnie wszytkie punkty w zasiegu jazdy jacka + 1 wrzucamy do kolejki priorytetowej
# wybieramy najkrotszy przejazd z kolejki - ma go przejechac marian
# do nowej kolejki wrzucamy wszystkie punkty przesiedkowe z zasiegu jazdy jacka + 1 od
# konca wybranej jazdy mariana i tak idziemy az skonczy sie tablica
# daje nam to zlozonosc O(nlogn) bo sortujemy tablice, a nastepnie przechodzac linowo po tablicy uzywamy heapq

def inny_pomysl(p, b):
    n = len(p)
    p.sort()
    przesiadkowe = []
    i = 0
    plen = len(przesiadkowe)
    for i in range(n):
        if p[i][1]:
            przesiadkowe.append(p[i][0])
    przesiadkowe.append(b)

    while i < len(p):
        heap = deque()
        for i in range(i, i+4):
            heap.append(-p[i])






def fun(p, b):
    n = len(p)
    p.sort()
    przesiadkowe = []
    i = 0
    plen = len(przesiadkowe)
    for i in range(n):
        if p[i][1]:
            przesiadkowe.append(p[i][0])

    lookup = [-1 for _ in range(len(przesiadkowe) + 1) for _ in range(2)]


    def rek(k, nk, marian):
        if k >= plen - 2 or k >= b:
            return 0

        if marian:
            wsp = 1
        else:
            wsp = 0


        if marian and nk - k == 3:
            return rek(k + 1, k + 1, True) + przesiadkowe[k + 1] - przesiadkowe[k] - 1

        if marian and nk - k > 3:
            return inf

        if marian:
            return

        return min(rek(k + 1, k + 1, True) + przesiadkowe[k + 1] - przesiadkowe[k] - 1, rek(k, k + 1, False))

    return rek(0, 0, False)


def drivers(P, B):
    r = fun(P, B)
    return [r]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(drivers, all_tests=False)
