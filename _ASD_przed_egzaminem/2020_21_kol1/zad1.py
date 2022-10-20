from zad1testy import runtests


# kopiuje tablice 2d do liniowej, robie quickselecta dla (N^2+N)/2 i (N^2-N)/2
# w ten sposob mam odpowiednio posortowana tablice jednowymiarowa, ktora liniowo przerzucam do 2D

def partition(tab, left, right):
    i = left - 1
    for j in range(left, right):
        if tab[j] < tab[right]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    i += 1
    tab[i], tab[right] = tab[right], tab[i]
    return i


def quick_select(tab, left, right, k):
    if left == right:
        return tab[left]
    if left < right:
        q = partition(tab, left, right)
        if q == k:
            return tab[q]
        elif q < k:
            return quick_select(tab, q + 1, right, k)
        else:
            return quick_select(tab, left, q - 1, k)


def Median(T):
    tlen = len(T)
    linear = [-1 for _ in range(tlen * tlen)]

    # przerzucam do liniowej
    for i in range(tlen * tlen):
        linear[i] = T[i // tlen][i % tlen]

    quick_select(linear, 0, tlen * tlen - 1, ((tlen * tlen + tlen) // 2) - 1)
    quick_select(linear, 0, tlen * tlen - 1, (tlen * tlen - tlen) // 2)

    lower_pointer = 0
    diagonal_pointer = (tlen * tlen - tlen) // 2
    higher_pointer = (tlen * tlen + tlen) // 2

    for i in range(tlen):
        for j in range(tlen):
            if i < j:
                T[i][j] = linear[higher_pointer]
                higher_pointer += 1
            if i == j:
                T[i][j] = linear[diagonal_pointer]
                diagonal_pointer += 1
            if i > j:
                T[i][j] = linear[lower_pointer]
                lower_pointer += 1


runtests(Median)
