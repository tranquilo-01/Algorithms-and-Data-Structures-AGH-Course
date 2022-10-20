def heapify(tab, n, i):
    # funkcja naprawia kopiec z jednym bledem pod indeksem tab[i]
    max_ind = i
    left = 2 * i
    right = 2 * i + 1
    if left < n and tab[max_ind] < tab[left]:
        max_ind = left
    if right < n and tab[max_ind] < tab[right]:
        max_ind = right
    if i != max_ind:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify(tab, n, max_ind)


def build_heap(tab):
    # funkcja buduje kopiec od zera uzywajac heapify()
    tlen = len(tab)
    for i in range(tlen // 2, -1, -1):
        heapify(tab, tlen, i)


def heap_sort(tab):
    tlen = len(tab)
    build_heap(tab)
    for i in range(tlen - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0)


arr = [18, 4, 13, 3, 8, 5, 23, 43, 5, 6, 7, 12, 123, 244, 235654, 1, 3, 4, 5, 2134, 3]
heap_sort(arr)
print(arr)
