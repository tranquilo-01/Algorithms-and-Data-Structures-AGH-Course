# Dana jest tablica A[n] z długosciami samochodów, które stoja w kolejce,
# zeby wjechac na prom. Prom ma dwa pasy (lewy i prawy), oba długosci L. Prosze napisac program, który
# wyznacza, które samochody powinny pojechac na który pas, zeby na promie zmiesciło sie jak najwiecej aut.
# Auta musza wjezdzac w takiej kolejnosci, w jakiej sa podane w tablicy A.

def laduj_rek(cars, i, left1, left2):
    res1 = res2 = 0
    if i > len(cars) - 1 or cars[i] > left1 and cars[i] > left2:
        return 0

    if cars[i] <= left1:
        res1 = laduj_rek(cars, i + 1, left1 - cars[i], left2)

    if cars[i] <= left2:
        res2 = laduj_rek(cars, i + 1, left1, left2 - cars[i])

    return max(res1, res2) + 1


def laduj_memo(cars, len1, len2):
    lookup = [[[-1 for _ in range(len2 + 1)] for _ in range(len1 + 1)] for _ in range(len(cars))]

    def rek(i, l1, l2):
        res1 = res2 = 0
        if i > len(cars) - 1 or cars[i] > l1 and cars[i] > l2:
            return 0

        if lookup[i][l1][l2] != -1:
            return lookup[i][l1][l2]

        if cars[i] <= l1:
            res1 = rek(i + 1, l1 - cars[i], l2)

        if cars[i] <= l2:
            res2 = rek(i + 1, l1, l2 - cars[i])

        lookup[i][l1][l2] = max(res1, res2) + 1
        return lookup[i][l1][l2]

    r = rek(0, len1, len2)
    return r


tab = [5, 4, 3, 3, 3, 2, 4, 8, 8, 3, 5, 4, 1, 4, 6, 2, 4, 5, 6, 5, 3, 2, 5, 1, 1, 2, 3, 6, 7, 8, 9]
l = 47
print(laduj_rek(tab, 0, l, l))
print(laduj_memo(tab, l, l))
