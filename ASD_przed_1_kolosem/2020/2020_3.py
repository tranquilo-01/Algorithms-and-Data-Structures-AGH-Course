# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga
# czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy.
# Zaproponowany algorytm powinien być możliwie jak najszybszy.
# Proszę oszacować jego złożoność obliczeniową.

# zlozonosc O(n^2)
# sortujemy tablice, a nstepnie dla kazdego elementu robimy klasyczny myk przesuwajac dwa wskazniki
# pierwszy wskaznik idzie od poczatku tablicy i gdy suma jest za mala przesuwa sie w prawo
# drugi wskaznik idzie od konca i gdy suma jest za duza przesuwa sie w lewo

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


def every_sum(tab):
    tlen = len(tab)
    quick_sort(tab, 0, tlen - 1)
    for ind in range(tlen):
        l = 0
        r = tlen - 1
        suma = tab[ind]
        while l < r:
            if l == ind or r == ind:
                if l == ind:
                    l += 1
                if r == ind:
                    r -= 1
            elif tab[l] + tab[r] < suma:
                l += 1
            elif tab[l] + tab[r] > suma:
                r -= 1
            else:
                break
        else:
            return False
    return True


arr = [-4, -2, -2, 0, -6, -8, 1, 3, 7, 2, 2, 4]
print(every_sum(arr))
