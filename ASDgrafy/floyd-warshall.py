# reprezentacja macierzowa
from math import inf


def floyd_warshall(graph):
    glen = len(graph)
    shortest = [[inf for _ in range(glen)] for _ in range(glen)]
    for i in range(glen):
        for j in range(glen):
            if i == j:
                shortest[i][j] = 0
            if graph[i][j] != 0:
                shortest[i][j] = graph[i][j]

    for k in range(0, glen):
        for u in range(glen):
            for v in range(glen):
                shortest[u][v] = min(shortest[u][v], shortest[u][k] + shortest[k][v])

    return shortest


graf = [[0, 7, 2, 0, 0, 0, 0, 0],
        [7, 0, 5, 0, 0, 0, 0, 0],
        [2, 0, 0, 6, 0, 0, 0, 18],
        [0, 5, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 12, 1, 0],
        [0, 0, 0, 0, 12, 0, 8, 0],
        [0, 0, 0, 0, 1, 8, 0, 0],
        [0, 0, 18, 0, 0, 0, 0, 0]]

wynik = floyd_warshall(graf)
for row in wynik:
    print(row)
 