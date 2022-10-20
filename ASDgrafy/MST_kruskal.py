# graf reprezentowany jako lista krawedzi [(k1, k2), waga]

class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x: Node):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x: Node, y: Node):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(graph):
    edges = sorted(graph, key=lambda e: e[1])
    glen = len(graph)
    mst = []
    nodes = []
    for i in range(glen):
        nodes.append(Node(i))

    for edge in edges:
        (start, end), weight = edge

        x = find(nodes[start])
        y = find(nodes[end])

        if x != y:  # nie ma cyklu
            mst.append(edge)
            union(x, y)

    return mst


graf = [[(0, 1), 7], [(1, 3), 5], [(3, 2), 6], [(2, 0), 2], [(2, 7), 18], [(3, 4), 1], [(4, 5), 12], [(5, 6), 8], [(4, 6), 1]]
print(kruskal(graf))
