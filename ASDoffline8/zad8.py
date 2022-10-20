from zad8testy import runtests
from math import ceil


from zad8testy import runtests
from math import sqrt, ceil


def length(a, b):
    x = (a[0] - b[0])
    y = (a[1] - b[1])
    return ceil(sqrt(x * x + y * y))


def highway(A):
    def find_parent(x):
        nonlocal parent
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal parent, count, tlen
        x = find_parent(x)
        y = find_parent(y)
        if x == y:
            return False
        if count[x] > count[y]:
            x, y = y, x
        parent[x] = y
        count[y] += count[x]
        if count[y] == tlen:
            return True

    def reset_tab():
        nonlocal parent, count, tlen
        parent = [k for k in range(tlen)]
        count = [1] * tlen

    # robie graf krawedzi posortowany rosnaco wg dlugosci
    tlen = len(A)
    edges = []
    for i in range(tlen):
        for j in range(i + 1, tlen):
            edges.append((length(A[i], A[j]), i, j))
    edges.sort()
    elen = len(edges)

    minInd = 0
    maxInd = elen - 1
    solution = edges[maxInd][0] - edges[minInd][0]
    parent = [j for j in range(tlen)]
    count = [1] * tlen

    while True:
        reset_tab()
        i = minInd
        while i < elen:
            _, x, y = edges[i]
            if union(x, y):
                solution = min(solution, edges[i][0] - edges[minInd][0])
                maxInd = i
                break
            i += 1
        else:
            break
        i = maxInd
        reset_tab()
        while i >= 0:
            _, x, y = edges[i]
            if union(x, y):
                solution = min(solution, edges[maxInd][0] - edges[i][0])
                minInd = i + 1
                break
            i -= 1
    return solution


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(highway, all_tests=True)
