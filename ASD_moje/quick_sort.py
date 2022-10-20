from time import time

from metody import naturalarray


def partition(tab, l, r):
    i = l - 1
    for j in range(l, r):
        if tab[j] <= tab[r]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]

    return i + 1


def quick_sort(tab, l, r):
    if l < r:
        q = partition(tab, l, r)
        quick_sort(tab, l, q - 1)
        quick_sort(tab, q + 1, r)



tablica = naturalarray(2*10**5, 0, 10**10)
t0 = time()
quick_sort(tablica, 0, len(tablica)-1)
t = time() - t0
print(t)
