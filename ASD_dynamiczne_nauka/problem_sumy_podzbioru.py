# Dana jest tablica n liczb naturalnych A. Prosze podac i zaimplementowac
# algorytm, który sprawdza, czy da sie wybrac podzbior liczb z A, które sumuja sie do zadanej
# wartosci T


def subset_sum(set, sum):
    n = len(set)

    # tablica z boolami, ktora informuje czy ze zbioru[0;el] da sie utworzyc sume s
    lookup = [[False for el in range(sum + 1)] for s in range(n + 1)]

    # sume rowa 0 zawsze da sie zrobic nie biorac nic
    for i in range(n + 1):
        lookup[i][0] = True

    # suma != 0 bo liczby naturalne
    for i in range(1, sum + 1):
        lookup[0][i] = False

    # jesli istnieje podzbior o 1 mniejszy z suma mniejsza o nasz aktualny element do dajemy True (przepisujac z tego miejsca w tablicy)
    # w przeciwnym wypadku dajemy false

    for i in range(1, n + 1):  # dla kazdego podzbioru [0; i]
        for j in range(1, sum + 1):  # sprawdzamy czy istnieje suma [0; j]
            if j < set[i - 1]:  # nie mozemy pomniejszyc o wiecej niz aktualna suma
                lookup[i][j] = lookup[i - 1][j]
            if j >= set[i - 1]:
                # wynik to {istnieje podzbior o 1 mniejszy o zadanej sumie, lub
                # istnieje podzbior o 1 mniejszy o sume rozniacej sie o aktualny element}
                lookup[i][j] = (lookup[i - 1][j] or lookup[i - 1][j - set[i - 1]])

    return lookup[n][sum]


print(subset_sum([2, 7, 3, 4], 9))
