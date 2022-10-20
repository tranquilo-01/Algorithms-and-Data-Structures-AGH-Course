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
    # f(i, p) = max(f(i-1, p), f(left[i], p-price[i]) + profit[i])

    n = len(T)


    lookup = [[-1 for _ in range(n)] for _ in range(p + 1)]  # tablica do spamietywania
    dorms = [T[i] + (i,) for i in range(len(T))]  # akademiki z indeksami, bo bedzie sortowane
    dorms.sort(key=lambda x: x[2])
    close_left = get_closest_left(dorms)
    profits = get_profits(T)
    prices = get_prices(T)

    print(dorms)

    def rek(i, ap):
        # print(i, ap)
        if ap <= 0 or i < 0:
            return 0

        if lookup[ap][i] != -1:
            return lookup[ap][i]

        lookup[ap][i] = max(rek(i - 1, ap), rek(close_left[i], ap - prices[dorms[i][4]]) + profits[dorms[i][4]])
        return lookup[ap][i]

    rek(len(T) - 1, p)
    for row in lookup:
        print(row)
    return [lookup[-1][-1]]


runtests(select_buildings)
