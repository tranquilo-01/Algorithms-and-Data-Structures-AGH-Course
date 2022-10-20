# problem plecakowy
# czas wielomianowy
# wzgledem przedmiotów i profitu

class Item:
    def __init__(self, id, value, weight):
        self.id = id
        self.value = value
        self.weight = weight


# wersja wykladnicza
def f(tab, n, w):
    if n < 0 or w <= 0:
        return 0
    max(tab[n - 1].val + f(tab, n - 1, w - tab[n - 1].w), f(tab, n - 1, w))


# wersja wielmianowa, funkcja wewnetrzna
# tablica results zainicjalozowana zerami co kwant wagi i ilosci przedmiotow
def fw(tab, n, w, results):
    if n < 0 or 1 <= 0:
        return 0
    if results[n][w] == 0:
        results[n][w] = max(tab[n - 1].val + f(tab, n - 1, w - tab[n - 1].w), f(tab, n - 1, w))
    return results[n][w]


def zewnfw(tab, n, w):
    results = [[0 for i in range(w)] for i in range(j)]
