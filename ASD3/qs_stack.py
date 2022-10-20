from random import randint
from time import time


def naturalarray(length, low, high):
    """uzupelnia tablice o podanej dlugosci liczbami naturalnymi w zakresie low - high"""
    array = []
    for i in range(length):
        array.append(randint(low, high))
    return array



def quicksort(tab):
    st = [(0, len(tab) - 1)]
    while len(st) > 0:
        p, r = st.pop()
        if p < r:
            q = partition(tab, p, r)
            st.append((p, q - 1))
            st.append((q + 1, r))


def partition(tab, p, r):
    i = p - 1
    # wszystkie elementy mniejsze od ostatniego ustawiamy na poczatek tablicy
    for j in range(p, r):
        if tab[j] <= tab[r]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    # zamieniamy pierwszy element wiekszy od ostatniego z ostatnim
    i += 1
    tab[i], tab[r] = tab[r], tab[i]
    return i


tablica = naturalarray(2*10**5, 0, 10**10)
t0 = time()
quicksort(tablica)
t = time() - t0
print(t)