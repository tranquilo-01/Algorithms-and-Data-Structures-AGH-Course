from zad7testy import runtests


def droga(G):
    visited = [False for _ in range(len(G))]
    s = []
    paths = []
    found = False

    def rek(graph, prev, v, vstd, path, pths):
        nonlocal found

        if found:  # jak cykl znalieziony to koniec
            return

        path.append(v)  # dodaje wierzcholek do kolejki

        if prev in graph[v][0]:  # sprawdzam ktora brama musze wyjsc
            out = 1
        else:
            out = 0

        if len(path) == len(graph):  # jesli dlugosc sciezki jest taka jak dlugosc grafu
            flag = False
            for u in graph[v][out]:  # to sprawdzam czy jest cyklem
                if u == 0:
                    flag = True
            if flag:
                for el in path:
                    pths.append(el)
                    found = True
                return

        vstd[v] = True  # wierzcholek odwiedzony

        for u in graph[v][out]:  # dla wszystkich nieodwiedzonych z dobrej bramy rekurencja
            if not vstd[u]:
                rek(graph, v, u, vstd, path, pths)

        vstd[v] = False  # powrot
        path.pop()

    rek(G, G[0][1][0], 0, visited, s, paths)
    if len(paths) > 0:
        return paths
    else:
        return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
