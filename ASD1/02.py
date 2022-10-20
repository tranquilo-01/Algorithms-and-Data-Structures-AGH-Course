# selection sort

def selection_sort(tab):
    tlen = len(tab)
    for i in range(tlen - 1):
        mini_pos = i
        for j in range(i + 1, tlen):
            if tab[i] < tab[mini_pos]:
                mini_pos = j
                tab[i], tab[mini_pos] = tab[mini_pos], tab[i]
