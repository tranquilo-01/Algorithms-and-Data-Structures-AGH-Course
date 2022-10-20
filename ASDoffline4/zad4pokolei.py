from zad4testy import runtests


def get_closest_left(dorms):
    """funkcja zwraca tablice najblizszych lewych sasiadow niepokrywajacych sie z danym akademikiem"""
    n = len(dorms)
    closest = [-1 for _ in range(n)]

    for i in range(n):
        for j in range(n - 1, -1, -1):
            if dorms[j][2] < dorms[i][1]:
                closest[i] = j
                break

    return closest


def get_profits(T):
    profits = [0 for _ in range(len(T))]
    for d in range(len(T)):
        p = T[d][0] * (T[d][2] - T[d][1])
        profits[d] = p

    return profits


def get_prices(T):
    prices = [0 for i in range(len(T))]
    for p in range(len(T)):
        prices[p] = T[p][3]
    return prices


def select_buildings(T, p):
    n = len(T)
    dorms = [T[i] for i in range(len(T))]  # akademiki z indeksami, bo bedzie sortowane
    dorms.sort(key=lambda x: x[2])
    closest_left = get_closest_left(dorms)
    lookup = [[-1 for _ in range(n)] for _ in range(p + 1)]  # tablica do spamietywania


    def rek(i, p):
        if p == 0 or i < 0:
            return 0

        return max()



runtests(select_buildings)
