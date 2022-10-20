import collections
from zad6testy import runtests


# trzeba znalezc najkrotsze sciezki z s do t. jezeli sa 2 rozlaczne to nie mozna usunac, jezeli jest jedna lub maja
# wspolny fragment to mozna usunac dowolny element ze wspolnego fragmentu
def longer(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    q = collections.deque()
    distance[s] = 0
    visited[s] = True
    q.append(s)
    tdist = 10 ** 10
    flag = False

    while q:
        u = q.pop()
        n = len(G[u])
        if flag:
            break
        for i in range(n):
            v = G[u][i]
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                q.appendleft(v)
                if visited[t] and not flag:
                    tdist = distance[v]
                    flag = True
    if not visited[t]:
        return None

    path = [[] for _ in range(tdist + 1)]
    path[tdist] = [t]
    for d in range(tdist, -1, -1):
        for v in path[d]:
            for u in G[v]:
                if distance[u] == d - 1 and u not in path[d - 1]:
                    path[d - 1].append(u)

    for i in range(len(path) - 1):
        if len(path[i]) == len(path[i + 1]) == 1:
            return path[i][0], path[i + 1][0]

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)

# graf = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
# longer(graf, 0, 7)
