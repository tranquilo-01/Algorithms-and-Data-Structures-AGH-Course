def dfs(graph):
    # reprezentacja listowa
    glen = len(graph)
    visited = [False for _ in range(glen)]
    parents = [-1 for _ in range(glen)]
    time = 0

    def dfs_visit(G, u):
        nonlocal time
        time += 1  # czas odwiedzenia
        visited[u] = True
        for w in G[u]:
            if not visited[w]:
                parents[w] = u
                dfs_visit(G, w)
        time += 1  # czas przetworzenia

    for v in range(glen):
        if not visited[v]:
            dfs_visit(graph, v)

    print(parents)


graf = [[1, 2], [0, 3], [0, 4, 5], [1, 5, 4], [2, 3, 6], [2, 3], [4, 7], [6]]
graf2 = [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3, 5, 6], [4, 6], [4, 5]]

dfs(graf2)
