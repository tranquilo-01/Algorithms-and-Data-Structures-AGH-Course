import heapq

from kol3btesty import runtests

# na razie pomyslem jest zmodyfikowanie grafu tak aby zrobic z niego graf, ktory ma takze polaczenia
# samolotowe jako krawedzie. wtedy wystarczy przejsc po tym grafie algorytmem dijkstry. zlozonosc jest
# O(n^2) przez modyfikacje grafu
from math import inf


def modify_graph(graph, s):
    slen = len(s)
    for w1 in range(slen):
        for w2 in range(slen):
            if w1 != w2:
                graph[w1].append((w2, s[w1] + s[w2]))


def airports(G, A, s, t):
    modify_graph(G, A)
    glen = len(G)
    dist = [inf for _ in range(glen)]
    parents = [-1 for _ in range(glen)]
    heap = []
    visited = [False for _ in range(glen)]

    def relax(ur, vr, wr):
        if dist[vr] > dist[ur] + wr:
            dist[vr] = dist[ur] + wr
            parents[vr] = ur

    dist[s] = 0
    visited[s] = True
    heap.append((s, 0))

    # dijkstra
    while heap:
        (w, u) = heapq.heappop(heap)
        visited[u] = True
        for vertex in G[u]:
            (v, wv) = vertex
            if not visited[v]:
                relax(u, v, wv)
                heapq.heappush(heap, (wv, v))

    print(dist)
    return dist[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
