import queue


def longer(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    q = queue.Queue()
    distance[s] = 0
    visited[s] = True
    q.put(s)
    tdist = 10 ** 10
    flag = False

    while not q.empty():
        u = q.get()
        n = len(G[u])
        if flag:
            break
        for i in range(n):
            v = G[u][i]
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                q.put(v)
                if visited[t] and not flag:
                    tdist = distance[v]
                    flag = True


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


graf = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6, 7], [5, 7], [5, 6, 8], [7]]

print(longer(graf, 0, 8))
