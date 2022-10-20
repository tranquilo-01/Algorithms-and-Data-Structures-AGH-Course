from zad3testy import runtests
# uruchamiamy dfs i po przetworzeniu wierzcholka dodajemy go na poczatek listy
from collections import deque


def topo_sort(graph):
    # reprezentacja listowa
    glen = len(graph)
    visited = [False for _ in range(glen)]
    topologia = deque()  # stworzenie listy na posortowane wierzcholki

    def dfs_visit(G, u):
        visited[u] = True

        for w in G[u]:
            if not visited[w]:
                dfs_visit(G, w)

        topologia.appendleft(u)  # dodawanie na poczatek listy

    for v in range(glen):
        if not visited[v]:
            dfs_visit(graph, v)

    return list(topologia)


def tasks(T):
    n = len(T)
    graph = [[] for _ in range(n)]
    for row in range(n):
        for el in range(n):
            if T[row][el] == 1:
                graph[row].append(el)
            if T[row][el] == 2:
                graph[el].append(row)
    print(graph)

    return topo_sort(graph)


runtests(tasks)
