# graf jako macierz sasiedztwa
# funkcja zwraca liste krawedzi
import heapq


def prim(graph):
    glen = len(graph)
    visited = [False for _ in range(glen)]
    mst = []
    heap = []

    v = 0
    visited[0] = True

    for i in range(glen):
        for u in range(glen):
            if graph[v][u] != 0 and not visited[u]:
                heapq.heappush(heap, (graph[v][u], (v, u)))

        while heap:
            (w, (x, y)) = heapq.heappop(heap)
            if not visited[y]:
                visited[y] = True
                mst.append(((x, y), w))
                v = y
                break

    return mst


graf = [[0, 7, 2, 0, 0, 0, 0, 0],
        [7, 0, 5, 0, 0, 0, 0, 0],
        [2, 0, 0, 6, 0, 0, 0, 18],
        [0, 5, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 12, 1, 0],
        [0, 0, 0, 0, 12, 0, 8, 0],
        [0, 0, 0, 0, 1, 8, 0, 0],
        [0, 0, 18, 0, 0, 0, 0, 0]]

print(prim(graf))
