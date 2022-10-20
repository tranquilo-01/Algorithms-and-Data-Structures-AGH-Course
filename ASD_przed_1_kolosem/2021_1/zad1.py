from copy import deepcopy

from zad1testy import runtests


# Dana jest dwuwymiarowa tablica T o rozmiarach N ×N wypełniona liczbami naturalnymi (liczby
# sa parami rózne). Prosze zaimplementowac funkcje Median(T), która przekształca tablice T, tak
# aby elementy lezace pod główna przekatna nie były wieksze od elementów na głównej przekatnej,
# a elementy lezace nad główna przekatna nie były mniejsze od elementów na głównej przekatnej.
# Algorytm powinien byc jak najszybszy oraz uzywac jak najmniej pamieci ponad te, która potrzebna
# jest na przechowywanie danych wejsciowych (choc algorytm nie musi działac w miejscu). Prosze
# podac złozonosc czasowa i pamieciowa zaproponowanego algorytmu

# Przykład. Dla tablicy:
# T = [ [ 2, 3, 5],
# [ 7,11,13],
# [17,19,23] ]
# wynikiem jest, miedzy innymi tablica:
# T = [ [13,19,23],
#       [ 3, 7,17],
#       [ 5, 2,11] ]


# zlozonosc liniowa:
# cala przekatna musi byc jakby "mediana"
# selectem z quick sorta znajdujemy element "a" ktory powinien byc na miejscu (n^2)/2 - (n/2) + 1
# i element "b" ktory powinien byc na miejscu (n^2)/2 + (n/2)
# wszystkie elementy mniejsze od a dajemy pod przekatna, wieksze od b nad przekatna, a pomiedzy a i b na przekatna

def partition(tab, l, r):
    i = l - 1
    n = len(tab)
    for j in range(l, r):
        if tab[j // n][j % n] < tab[r // n][r % n]:
            i += 1
            tab[i // n][i % n], tab[j // n][j % n] = tab[j // n][j % n], tab[i // n][i % n]

    i += 1
    tab[i // n][i % n], tab[r // n][r % n] = tab[r // n][r % n], tab[i // n][i % n]
    return i


def quick_sort(tab, l, r):
    if l < r:
        pivot = partition(tab, l, r)
        quick_sort(tab, l, pivot - 1)
        quick_sort(tab, pivot + 1, r)


def select(tab, l, r, k):
    n = len(tab)
    if l == r:
        return tab[l // n][l // n]
    if l < r:
        q = partition(tab, l, r)
        if q == k:
            return tab[q // n][q % n]
        elif q < k:
            return select(tab, q + 1, r, k)
        else:
            return select(tab, l, q - 1, k)


def median(tab):
    n = len(tab)
    a = select(tab, 0, n * n - 1, (n * n) / 2 - (n / 2))
    b = select(tab, 0, n * n - 1, (n * n) / 2 + (n / 2) - 1)
    diag = [[0 for _ in range(n)] for z in range(n)]
    diag_ind = 0
    over_iterator = 0
    under_iterator = n * n - 1
    for row in range(n):
        for el in range(n):
            if a <= tab[row][el] <= b and diag_ind < n:
                diag[diag_ind][diag_ind] = tab[row][el]
                diag_ind += 1
            elif tab[row][el] > b:
                done = False
                while not done:
                    if over_iterator // n < over_iterator % n:
                        diag[over_iterator // n][over_iterator % n] = tab[row][el]
                        done = True
                    over_iterator += 1
            elif tab[row][el] < a:
                done = False
                while not done:
                    if under_iterator // n > under_iterator % n:
                        diag[under_iterator // n][under_iterator % n] = tab[row][el]
                        done = True
                    under_iterator -= 1

    for x in range(n):
        for y in range(n):
            tab[x][y] = diag[x][y]



runtests(median)