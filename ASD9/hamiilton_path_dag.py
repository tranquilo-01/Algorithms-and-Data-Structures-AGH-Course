# sortowanie topologiczne, potem liniowe przejscie
# po posortowaniu sprawdzamy czy mozemy przejsc z kazdego wierzcholka do jego nastepika po pososrtowaniu
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


def is_ham_path(graph):
    topo_sorted_list = topo_sort(graph)
    glen = len(topo_sorted_list)
    for i in range(glen-1):
        if topo_sorted_list[i+1] not in graph[topo_sorted_list[i]]:
            return False
    return True


graf = [[1, 2, 5], [2, 4], [], [], [3, 6, 5], [], []]
graf2 = [[1], [2], [3], []]
lista = (topo_sort(graf))
print(lista)
print(is_ham_path(graf2))
