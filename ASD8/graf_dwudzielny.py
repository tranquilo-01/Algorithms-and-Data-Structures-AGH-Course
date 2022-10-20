# dla grafu spojnego
# zrobimy BFSem z lista sasiedztwa
# O(V+E)

import queue


def is_bipartitive(G):
    n = len(G)
    visited = [False for _ in range(n)]
    part = [None for _ in range(n)]
    visited[0] = True
    part[0] = True
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for i in range(len(G[u])):
            if visited[G[u][i]]:
                if part[G[u][i]] == part[u]:
                    return False
            else:
                visited[G[u][i]] = True
                part[G[u][i]] = not part[G[u][u]]
                q.put(G[u][i])
    return True
