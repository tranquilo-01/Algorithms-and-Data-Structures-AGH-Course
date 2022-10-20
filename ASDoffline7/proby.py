from zad7testy import runtests


def droga(G):
    visited = [False for _ in range(len(G))]  # tablica odwiedzonych wierzcholkow
    path = []  # stos w ktorym zapisywany bedzie cykl

    def roam_around(graph, prev, v):
        if prev in graph[v][0]:  # sprawdzam ktora brama musze wyjsc
            out = 1
        else:
            out = 0

        path.append(v)

        if len(path) == len(graph):
            flag = False

            for u in graph[v][out]:
                if u == 0:
                    flag = True
            if flag:
                return path

        visited[v] = True

        for u in graph[v][out]:
            if not visited[u]:
                return roam_around(graph, v, u)

        visited[v] = False
        path.pop()

    return roam_around(G, 0, G[0][0])


def rek(graph, prev, v, visited, s):
    s.append(v)

    if prev in graph[v][0]:  # sprawdzam ktora brama musze wyjsc
        out = 1
    else:
        out = 0

    if len(s) == len(graph):
        flag = False
        for u in graph[v][out]:
            if u == 0:
                flag = True
        if flag:
            print("cyc")
        else:
            print("pat")
        print(s)
        s.pop()
        return

    visited[v] = True

    for u in graph[v][out]:
        if not visited[u]:
            rek(graph, v, u, visited, s)

    visited[v] = False
    s.pop()


runtests(droga, all_tests=False)
