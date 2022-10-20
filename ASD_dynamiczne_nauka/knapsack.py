def knapsack(weights, prices, w):
    n = len(weights)
    lookup = [[0 for b in range(w + 1)] for i in range(n)]  # tablica przachowujaca wartosci plecaka [do tego elementu][uzyta waga]

    for wght in range(weights[0], w + 1):  # uzupelnienie pierwszego rzedu
        lookup[0][wght] = prices[0]

    for i in range(1, n):  # funkcja rekurencyjna zrobiona iteracyjnie na tablicy
        for wght in range(w + 1):
            lookup[i][wght] = lookup[i - 1][wght]
            if wght - weights[i] >= 0:
                lookup[i][wght] = max(lookup[i - 1][wght], lookup[i - 1][wght - weights[i]] + prices[i])

    to_return = []
    col = col_tmp = w

    for row in range(n - 1, 0, -1):  # odzyskiwanie wybranych przedmiotow
        col = col_tmp
        if lookup[row][col] == lookup[row - 1][col]:
            continue
        else:
            to_return.append(row)
            col_tmp = col
            while lookup[row - 1][col_tmp] != lookup[row][col] - prices[row]:
                col_tmp -= 1

    if lookup[0][col] != 0:
        to_return.append(0)

    for row in lookup:
        print(row)

    print(to_return)
    return lookup[-1][-1]


weights = [1, 2, 3]
prices = [60, 10, 120]
w = 5

print(knapsack(weights, prices, w))
