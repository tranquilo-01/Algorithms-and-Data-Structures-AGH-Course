# na grafie skierowanym
# robimy dfs zapamietujac czasy przetworzenia wierzcholkow
# odwracamy kierunek wszystkich krawedzi
# wykonujemy kolejny dfs w kolejnosci malejacych czasow przetworzenia
# algorytm Korsaraju

def transpose(graph):
    """funkcja transponujaca graf skierowany"""
    glen = len(graph)
    graph_t = [[] for _ in range(glen)]

    for v in range(glen):
        for u in graph[v]:
            graph_t[u].append(v)

    return graph_t


def korsaraju(graph):
    """zwraca liste list spojnych skladowych"""
    # reprezentacja listowa
    # przygotowanie
    glen = len(graph)
    visited = [False for _ in range(glen)]
    stack = []
    scc = []

    def dfs_order(G, u):
        """przechodzi DFSem i odklada na stack w kolejnosci przetworzenia"""
        visited[u] = True
        for w in G[u]:
            if not visited[w]:
                dfs_order(G, w)
        stack.append(u)

    def dfs_reverse(G, u):
        """przyjmuje transponowany graf i przechodzi po nim od konca stacku
        dodajac wierzcholki do odpowiednich list"""
        visited[u] = True
        scc[-1].append(u)
        for w in G[u]:
            if not visited[w]:
                dfs_reverse(G, w)

    # glowny kod funkcji
    for v in range(glen):
        if not visited[v]:
            dfs_order(graph, v)

    transposed = transpose(graph)
    visited = [False for _ in range(glen)]

    while stack:
        v = stack.pop()
        if not visited[v]:
            scc.append([])
            dfs_reverse(transposed, v)

    return scc


graf = [[3, 2], [0], [1], [4], []]
print(korsaraju(graf))
