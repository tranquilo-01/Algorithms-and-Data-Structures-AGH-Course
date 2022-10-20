from collections import deque


def bfs(G, s):
    glen = len(G)
    visited = [False for _ in range(glen)]
    distance = [-1 for _ in range(glen)]
    parents = [-1 for _ in range(glen)]
    q = deque()

    q.append(s)
    distance[s] = 0
    visited[s] = True

    while q:
        u = q.pop()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parents[v] = u
                q.appendleft(v)

    print(distance)
    print(parents)


graf = [[1, 2], [0, 4], [0, 3, 5], [2, 4], [1, 3, 5], [2, 4, 6], [5, 7], [6]]
bfs(graf, 0)
