def insertion_sort(tab):
    tlen = len(tab)
    for i in range(1, tlen):
        key = tab[i]

        j = i - 1
        while j > -1 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key


