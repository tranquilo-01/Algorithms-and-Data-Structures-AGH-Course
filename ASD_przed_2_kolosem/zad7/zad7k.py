from zad7ktesty import runtests


def get_costs(trees, roots):
    """funkcja uzywa DFSa do znalezienia sumy litrow potrzebnych do podlania kazdego drzewa"""
    visited = [[False for _ in range(len(trees[0]))] for _ in range(len(trees))]
    prices = [0 for _ in range(len(roots))]
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    def dfs_visit(x, y, t):
        if 0 <= x < len(trees) and 0 <= y < len(trees[0]) and not visited[x][y] and trees[x][y] != 0:
            prices[t] += trees[x][y]
            visited[x][y] = True
            for move in moves:
                dfs_visit(x + move[0], y + move[1], t)

    for i in range(len(roots)):
        dfs_visit(0, roots[i], i)

    return prices


def ogrodnik(T, D, incomes, limit):
    n = len(incomes)
    costs = get_costs(T, D)
    # print(costs)
    # print(incomes)
    # print(limit)

    lookup = [[0 for _ in range(limit + 1)] for _ in range(n)]

    for i in range(limit + 1):
        if i - costs[0] >= 0:
            lookup[0][i] = incomes[0]

    for cst in range(1, limit + 1):
        for item in range(1, n):
            lookup[item][cst] = lookup[item - 1][cst]
            if cst - costs[item] >= 0:
                lookup[item][cst] = max(lookup[item - 1][cst], lookup[item - 1][cst - costs[item]] + incomes[item])

    # for row in lookup:
    #     print(row)

    return lookup[n - 1][limit]


runtests(ogrodnik, all_tests=True)
