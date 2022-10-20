def find_bridges(graph):
    # reprezentacja listowa
    glen = len(graph)
    visited = [False for _ in range(glen)]
    parents = [-1 for _ in range(glen)]
    bridges = []
    low = [-1 for _ in range(glen)]
    d = [-1 for _ in range(glen)]
    time = 1

    def dfs_visit(G, u):
        nonlocal time
        low[u] = d[u] = time
        time += 1
        visited[u] = True
        for w in G[u]:
            if not visited[w]:
                parents[w] = u
                dfs_visit(G, w)
                low[u] = min(low[u], low[w])  # dziecko
            if visited[w] and parents[u] != w:
                low[u] = min(low[u], d[w])  # krawedz wsteczna

        if low[u] == d[u] and parents[u] != -1:
            bridges.append((u, parents[u]))

    for v in range(glen):
        if not visited[v]:
            dfs_visit(graph, v)

    return bridges


graf = [[1, 2], [0, 3], [0, 4, 5], [1, 5, 4, 6], [2, 3, 6], [2, 3], [4, 7, 3], [6, 8], [7, 9], [8, 7]]
graf2 = [[1, 2], [0, 3], [0, 3, 7], [1, 2, 4], [3, 5, 6], [4, 6], [4, 5], [2]]

print(find_bridges(graf))
