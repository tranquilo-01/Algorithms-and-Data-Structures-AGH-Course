import heapq
from math import inf
from random import randint


def dijkstra_matrix(G, v):
    """dijkstra na macierzy sasiadztwa"""
    n = len(G)
    visited = [False] * n
    distance = [inf] * n
    parent = [-1] * n
    distance[v] = 0

    while True:
        visited[v] = True
        next_v = -1
        min_d = inf

        # znajdowanie krawędzi kolejnej
        for i in range(n):
            if visited[i]:
                continue
            # aktualizcja minimalnej odlegosci sasiadow
            if G[v][i] != 0 and distance[i] > distance[v] + G[v][i]:
                distance[i] = distance[v] + G[v][i]
                parent[i] = v
            # wybranie nastepengeo rozpatrywanego wierzcholka (takiego z min odlegloscia)
            if distance[i] < min_d:
                next_v = i
                min_d = distance[i]

        if next_v == -1:  # jezeli jest -1 to wszystkie wierzcholki dostpene z v sa odwiedzone( nie sprawdza spojnosci)
            # return distance, parent
            return distance

        v = next_v


def dijkstra_list(G, s):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    heap = []
    visited = [False for _ in range(n)]

    def relax(ur, vr, wr):
        if distance[vr] > distance[ur] + wr:
            distance[vr] = distance[ur] + wr
            parent[vr] = ur

    distance[s] = 0
    visited[s] = True
    heap.append((0, s))

    # dijkstra
    while heap:
        (w, u) = heapq.heappop(heap)
        visited[u] = True
        for vertex in G[u]:
            (v, wv) = vertex
            if not visited[v]:
                relax(u, v, wv)
                heapq.heappush(heap, (wv, v))

    return distance


def generate_graph(v_number, e_number, max_weight):
    graph = [[0 for _ in range(v_number)] for _ in range(v_number)]
    for i in range(e_number):
        w = randint(1, max_weight)
        v1 = randint(0, v_number - 1)
        v2 = randint(0, v_number - 1)
        graph[v1][v2] = w
        graph[v2][v1] = w

    return graph


graf = [[0, 7, 2, 0, 0, 0, 0, 0],
        [7, 0, 5, 0, 0, 0, 0, 0],
        [2, 0, 0, 6, 0, 0, 0, 18],
        [0, 5, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 12, 1, 0],
        [0, 0, 0, 0, 12, 0, 8, 0],
        [0, 0, 0, 0, 1, 8, 0, 0],
        [0, 0, 18, 0, 0, 0, 0, 0]]

graf2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
