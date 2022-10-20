# robimy dfsa tylko zamiast uzywac visited usuwamy krawedz ktora przeszlismy
# implemantacja dziala ale chyba powinno sie to zrobic inaczej na porzadnie
# lepiej jest w reprezetacji macierzowej, wtedy usuwamy zmieniajac 1 na 0
# funkcja zaklada ze graf ma cykl eulera


def find_eulerian_circuit(graph):
    # reprezentacja listowa
    glen = len(graph)
    # parents = [-1 for _ in range(glen)]
    # time = 0
    circuit = []

    def dfs_visit(G, u):
        # nonlocal time
        # time += 1
        for w in G[u]:
            # parents[w] = u
            G[u].remove(w)  # to sie pewnie jakos lepiej implementuje
            G[w].remove(u)
            dfs_visit(G, w)
        # time += 1
        circuit.append(u)

    for v in range(glen):
        if len(graph[v]) > 0:
            dfs_visit(graph, v)

    return circuit


graf = [[1, 2], [0, 2, 3, 5], [0, 1, 3, 5], [1, 2, 4, 5], [3, 5], [1, 2, 3, 4]]
print(find_eulerian_circuit(graf))
