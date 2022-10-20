# najkrotsze sciezki z ujemnymi wagami
# troche bez sensu implementacja na macierzy, tutaj zakladam ze nie moze istniec waga 0
from math import inf


def bellman_ford(graph, s):
    glen = len(graph)
    distance = [inf for _ in range(glen)]
    parent = [-1 for _ in range(glen)]

    def relax(x, y):
        if distance[y] > distance[x] + graph[x][y]:
            distance[y] = distance[x] + graph[x][y]
            parent[y] = x

    distance[s] = 0

    for i in range(glen - 1):
        for u in range(glen):
            for v in range(glen):
                if graph[u][v] != 0:
                    relax(u, v)

    for u in range(glen):
        for v in range(glen):
            if graph[u][v] != 0:
                if distance[v] > distance[u] + graph[u][v]:
                    return False
    return distance


graf = [[0, -5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 18],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 12, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]


print(bellman_ford(graf, 0))
