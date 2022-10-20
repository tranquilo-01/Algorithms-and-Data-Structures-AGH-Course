from egz1btesty import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = 0  # pole do wykorzystania przez studentow


# Krzysztof Dziechciarz 408059
# dla kazdego node zapisuje jego "glebokosc" w drzewie
# nastepnie na podtstawie danych o glebeokosci kazdego node zliczam ilosc nodeow i lisci na kazdej glebokosci
# i zapisuje te dane w odpowiednich tablicach
# idac od najwiekszej glebokosci szukam poziomu n na ktorym jest najwiecej nodeow i jednoczesnie jest to najglebszy
# poziom o tej ilosci nodeow
# odcinam wszystkie krawedzie miedzy poziomem n a n+1
# nastepnie odcinam poddrzewa ktore koncza sie liscmi na mniejszej glebokosci niz n
# wszystkie operacje sa wykonywane w czasie liniowym, wiec zlozonosc czasowa algorytmu to O(n)

def wideentall(T):
    max_depth = 0

    def calculate_depths(root: Node):
        nonlocal max_depth
        max_depth = max(max_depth, root.x)
        if root.right is not None:
            root.right.x = root.x + 1
            calculate_depths(root.right)
        if root.left is not None:
            root.left.x = root.x + 1
            calculate_depths(root.left)

    T.x = 0
    calculate_depths(T)

    nodes_at_level = [0 for _ in range(max_depth + 1)]
    leaves_at_level = [0 for _ in range(max_depth + 1)]
    nodes_at_level[0] = 0
    leaves_at_level[0] = 0

    def process_arrays(root: Node):
        nodes_at_level[root.x] += 1
        if root.left is None and root.right is None:
            leaves_at_level[root.x] += 1
        if root.left is not None:
            process_arrays(root.left)
        if root.right is not None:
            process_arrays(root.right)

    process_arrays(T)

    # szukam maksymalnej ilosci nodeow na jak najwyzszym poziomie
    max_node_quantity = 0
    max_node_quantity_level = -1
    for n in range(max_depth, -1, -1):
        if nodes_at_level[n] > max_node_quantity:
            max_node_quantity = nodes_at_level[n]
            max_node_quantity_level = n

    result = 0
    # aby zrobic drzewo ladnym usuwam wszystkie krawedzie ponizej poziomu max_node_quantity_level
    if max_depth >= max_node_quantity_level + 1:
        result += nodes_at_level[max_node_quantity_level + 1]

    # rekurencyjnie obliczam maksymalny poziom liscia poddrzewa
    def max_subtree_leave_level(root: Node):
        if root.left is None and root.right is None:
            return root.x
        lx = rx = 0
        if root.left is not None:
            lx = max_subtree_leave_level(root.left)
        if root.right is not None:
            rx = max_subtree_leave_level(root.right)
        if root.left is not None and root.right is not None:
            root.x = max(lx, rx)
            return root.x
        if root.left is None:
            root.x = rx
            return rx
        if root.right is None:
            root.x = lx
            return lx

    max_subtree_leave_level(T)

    # usuwam poddrzewa zakonczone lisciem o maksymalnej glebokosci mniejszej niz glebokosc docelowego drzewa
    def remove_remaining_leaves(root: Node):
        nonlocal result
        if root.x is not None and root.x < max_node_quantity_level:
            result += 1
        else:
            if root.left is not None:
                remove_remaining_leaves(root.left)
            if root.right is not None:
                remove_remaining_leaves(root.right)

    remove_remaining_leaves(T)

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=True)

