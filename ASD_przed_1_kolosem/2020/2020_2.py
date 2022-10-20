# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

# obliczymy wzrost na pozycji p i q quick selectem
# zwracamy tablicę zawierającą elementy na pozycjach od p do q w wejsciowej tablicy
# dwa wywyolania quick selecta sprawiaja ze pomiedzy indeksami p i q sa elementy wieksze od p i mniejsze od q
# zlozonosc O(n)


def partition(tab, l, r):
    i = l - 1
    for j in range(l, r):
        if tab[j] < tab[r]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    i += 1
    tab[i], tab[r] = tab[r], tab[i]
    return i


def quick_select(tab, ind, l, r):
    if l == r:
        return tab[l]
    if l < r:
        q = partition(tab, l, r)
        if q == ind:
            return tab[q]
        elif q < ind:
            return quick_select(tab, ind, q + 1, r)
        else:
            return quick_select(tab, ind, l, q - 1)


def section(tab, p, q):
    result = []
    quick_select(tab, p, 0, len(tab)-1)
    quick_select(tab, q, 0, len(tab)-1)
    for height in range(p, q+1):
        result.append(tab[height])
    print(tab)
    return result


arr = [2, 1, 3, 7, 777, 444, 555, 222, 778, 999, 4, 20, 6, 9, 324, 213, 436, 12, 3245, 13, 8756, 2314, 2131, 546, 235, 2134, 756, 124, 4326, 129, 4325234, 2352345, 52345]
print(section(arr, 4, len(arr)-4))
