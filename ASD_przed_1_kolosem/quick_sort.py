def quick_sort(tab, l, r):
    if l < r:
        pivot = partition(tab, l, r)
        quick_sort(tab, l, pivot - 1)
        quick_sort(tab, pivot + 1, r)


def partition(tab, l, r):
    i = l - 1
    for j in range(l, r):
        if tab[j] < tab[r]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    i += 1
    tab[i], tab[r] = tab[r], tab[i]
    return i

