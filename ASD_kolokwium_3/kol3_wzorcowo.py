import heapq

from kol3btesty import runtests

# do grafu dodaje wierzcholek ktory bedzie "przestrzenia powietrzna", do ktorego krawedzia o odpowiedniej wadze dolacze
# kazde lotnisko
# zlozonosc O(n+m)log(n)

from math import inf


# dodaje wierzcholek "przestrzen powietrzna
def modify_graph(graph, s):
    slen = len(s)
    graph.append([])
    for i in range(slen):
        graph[-1].append((i, s[i]))
        graph[i].append((slen, s[i]))


def airports(G, A, s, t):
    modify_graph(G, A)
    glen = len(G)
    dist = [inf for _ in range(glen)]
    parents = [-1 for _ in range(glen)]
    heap = []
    visited = [False for _ in range(glen)]

    def relax(ur: int, vr: int, wr: int):
        if dist[vr] > dist[ur] + wr:
            dist[vr] = dist[ur] + wr
            parents[vr] = ur

    dist[s] = 0
    visited[s] = True
    heap.append((0, s))

    # dijkstra
    while heap:
        (w, u) = heapq.heappop(heap)
        visited[u] = True
        for vertex in G[u]:
            (v, wv) = vertex
            if not visited[v]:
                heapq.heappush(heap, (wv, v))
                relax(u, v, wv)

    print(dist)
    print(parents)
    return dist[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
