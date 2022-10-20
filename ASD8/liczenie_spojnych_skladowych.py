# DFS z reprezentacja macierzowa
# O(v^2)

from collections import deque


def dfs(G):
    counter = 0
    visited = [False for _ in range(len(G))]
    for i in range(len(G)): # zewnetrzna petla do zliczania skladowych z dfsem w srodku
        if not visited[i]:
            visited[i] = True
            counter += 1
            s = deque()
            s.append(i)
            while not len(s) > 0:
                u = s.pop()
                for v in range(len(G[u])):
                    if G[u][v] and not visited[v]:
                        visited[v] = True
                        s.append(v)
    return counter


