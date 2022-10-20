# uruchamiamy dfs i po przetworzeniu wierzcholka dodajemy go na poczatek listy
from collections import deque


def topo_sort(graph):
    # reprezentacja listowa
    glen = len(graph)
    visited = [False for _ in range(glen)]
    # parents = [-1 for _ in range(glen)]
    # time = 0
    topologia = deque()  # stworzenie listy na posortowane wierzcholki

    def dfs_visit(G, u):
        # nonlocal time
        # time += 1
        visited[u] = True
        for w in G[u]:
            if not visited[w]:
                # parents[w] = u
                dfs_visit(G, w)
        # time += 1
        topologia.appendleft(u)  # dodawanie na poczatek listy

    for v in range(glen):
        if not visited[v]:
            dfs_visit(graph, v)

    return list(topologia)


graf = [[1, 2, 5], [2, 4], [], [], [3, 6, 5], [], []]
print(topo_sort(graf))
