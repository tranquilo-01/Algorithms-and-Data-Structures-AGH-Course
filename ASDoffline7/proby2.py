import sys

from zad7testy import runtests
from collections import deque


def rek(graph, prev, v, visited, path, paths):
    path.append(v)

    if prev in graph[v][0]:  # sprawdzam ktora brama musze wyjsc
        out = 1
    else:
        out = 0

    if len(path) == len(graph):
        flag = False
        for u in graph[v][out]:
            if u == 0:
                flag = True
        if flag:
            for el in path:
                paths.append(el)
            return

    visited[v] = True

    for u in graph[v][out]:
        if not visited[u]:
            rek(graph, v, u, visited, path, paths)

    visited[v] = False
    path.pop()


def droga(G):
    visited = [False for _ in range(len(G))]
    s = []
    paths = []
    found = False
    rek(G, G[0][0][0], 0, visited, s, paths)
    if len(paths) > 0:
        return paths
    else:
        return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)