import heapq
from math import inf


# algorytm na macierzy sasiedztwa


def dijkstra(graph, s):
    glen = len(graph)
    visited = [False for _ in range(glen)]
    parents = [-1 for _ in range(glen)]
    distances = [inf for _ in range(glen)]

    # heap = []

    def relax(x, y):
        if distances[y] > distances[x] + graph[x][y]:
            distances[y] = distances[x] + graph[x][y]
            parents[y] = x

    visited[s] = True
    distances[s] = 0

    for x in range(glen):
        w = min(graph[x])
        visited[w] = True
        for y in range(glen):
            if graph[x][y] > 0 and visited[y] == False and distances[y] > distances[x] + graph[x][y]:
                distances[y] = distances[x] + graph[x][y]
                parents[x] = y

    return distances


def dijkstra_zly(graph, s):
    glen = len(graph)
    visited = [False for _ in range(glen)]
    parents = [-1 for _ in range(glen)]
    distances = [inf for _ in range(glen)]
    heap = []

    def relax(x, y):
        if distances[y] > distances[x] + graph[x][y]:
            distances[y] = distances[x] + graph[x][y]
            parents[y] = x

    visited[s] = True
    distances[s] = 0
    heap.append((s, 0))

    while heap:
        (w, u) = heapq.heappop(heap)
        visited[u] = True
        for v in range(glen):
            if graph[u][v] != 0 and not visited[v]:
                heapq.heappush(heap, (graph[u][v], v))
                relax(u, v)

    return distances


graf = [[0, 7, 2, 0, 0, 0, 0, 0],
        [7, 0, 5, 0, 0, 0, 0, 0],
        [2, 0, 0, 6, 0, 0, 0, 18],
        [0, 5, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 12, 1, 0],
        [0, 0, 0, 0, 12, 0, 8, 0],
        [0, 0, 0, 0, 1, 8, 0, 0],
        [0, 0, 18, 0, 0, 0, 0, 0]]

print(dijkstra_zly(graf, 1))
print(dijkstra(graf, 1))
