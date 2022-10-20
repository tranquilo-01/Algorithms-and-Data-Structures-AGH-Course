from zad1testy import runtests


# nlogn wzorcowa
# stworze noea tablice krotek o rozmiarze takim samym jak pierwotna
# uzupelnie ja krotkami (liczba, index), gdzie index to pozycja z pierwotne
# posortuje tablice
# przejde liniowo i sprawdze jaka jest maksymalna roznica miedzy indexem w posortowanej a pierwotnej

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


def chaos_index(T: list):
    tlen = len(T)
    new = [(T[i], i) for i in range(tlen)]

    quick_sort(new, 0, tlen - 1)

    maxx = 0
    for i in range(tlen):
        maxx = max(abs(new[i][1] - i), maxx)

    return maxx


runtests(chaos_index)
