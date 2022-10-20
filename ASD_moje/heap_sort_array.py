def right(i):
    return 2 * i + 2


def left(i):
    return 2 * i + 1


def parent(i):
    return (i - 1) // 2


def heapify(tab, n, i):
    # funkcja naprawia kopiec z jednym błędem dla elementów poniżej i do n
    max_ind = i  # indeks najwiekszego elementu, na poczatku zakladmy ze kopiec git
    r = right(i)
    l = left(i)
    if l < n and tab[l] > tab[max_ind]:
        max_ind = l
    if r < n and tab[r] > tab[max_ind]:
        max_ind = r
    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify(tab, n, max_ind)


def build_heap(tab):
    tlen = len(tab)
    n = parent(tlen - 1)
    for i in range(n, -1, -1):
        heapify(tab, tlen, i)


def heap_sort(tab):
    tlen = len(tab)
    build_heap(tab)
    for i in range(tlen - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0)


def heapify_k_chaotic(tab, n, i, k, counter=0):
    # funkcja naprawia kopiec z jednym błędem dla elementów poniżej i do n
    max_ind = i  # indeks najwiekszego elementu, na poczatku zakladmy ze kopiec git
    r = right(i)
    l = left(i)
    if l < n and tab[l] > tab[max_ind] and counter <= k:
        max_ind = l
    if r < n and tab[r] > tab[max_ind] and counter <= k:
        max_ind = r
    if max_ind != i and counter <= k:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify_k_chaotic(tab, n, max_ind, k, counter + 1)


def build_heap_k_chaotic(tab, k):
    tlen = len(tab)
    n = parent(tlen - 1)
    for i in range(n, -1, -1):
        heapify_k_chaotic(tab, tlen, i, k)


def heap_sort_k_chaotic(tab, k):
    tlen = len(tab)
    build_heap_k_chaotic(tab, k)
    for i in range(tlen - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify_k_chaotic(tab, i, 0, k)

# tablica = [5, 7, 4, 3, 1, 2, 9, 6, 5]
# build_heap(tablica)
# print(tablica)
