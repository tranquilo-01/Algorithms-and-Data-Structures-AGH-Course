# Dane jest drzewo T zawierające n wierzchołków. Każda krawędź e drzewa ma wagę w(e) ∈ N oraz unikalny
# identyfikator id(e) ∈ N. Wagą drzewa jest suma wag jego krawędzi. Proszę napisać funkcję:
# def balance(T):
#     ...
# która zwraca identyfikator takiej krawędzi e drzewa, że usunięcie e dzieli drzewo na takie dwa,
# których różnica wag jest minimalna. Proszę szacować złożoność czasową i pamięciową użytego algorytmu.
# Reprezentacja drzewa.
# Drzewo reprezentowane jest przy pomocy węzłów typu Node:
# class Node:
#     def __init__(self):  # stwórz węzeł drzewa
#         self.edges = []  # lista węzłów do których są krawędzie
#         self.weights = []  # lista wag krawędzi
#         self.ids = []  # lista identyfikatorów krawędzi
#
#     def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
#         self.edges.append(x)  # o wadze w i identyfikatorze id
#         self.weights.append(w)
#         self.ids.append(id)
# Pole edges zawiera listę obiektów typu Node. Pola edges, weights oraz ids to listy równej długości.
# Należy założyć, że drzewo ma conajmniej jedną krawędź. Dopuszczalne jest dopisywanie własnych
# pól do Node.
from zad2testy import runtests
from math import inf


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.sum_of_edges = 0

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)


def sum_weights(root: Node):
    if len(root.edges) > 0:
        for e in root.edges:
            sum_weights(e)
            root.sum_of_edges += e.sum_of_edges
        for w in root.weights:
            root.sum_of_edges += w


def find_result(root: Node):
    sum_weights(root)
    suma = root.sum_of_edges
    min_dif = inf
    min_id = -1

    def rek(r: Node):
        nonlocal suma, min_dif, min_id
        for i in range(len(r.edges)):
            if abs(suma - 2 * r.edges[i].sum_of_edges - r.weights[i]) < min_dif:
                min_dif = abs(suma - 2 * r.edges[i].sum_of_edges - r.weights[i])
                min_id = r.ids[i]

    rek(root)

    return min_id


def balance(T: Node):
    res = find_result(T)
    return res


runtests(balance)
