def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q - 1)
        quicksort(tab, q + 1, r)


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



