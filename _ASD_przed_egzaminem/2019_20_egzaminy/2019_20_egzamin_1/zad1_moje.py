from math import inf
from zad1testy import runtests


# Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
# Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
# na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
# opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
# transportu na inny oraz minimalizuje koszt podróży.
# Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
# oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
# zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
# nie istnieje, funkcja powinna zwrócić wartość None.


def islands(G, A, B):
    glen = len(G)
    visited = [False for _ in range(glen)]
    distance = [inf for _ in range(glen)]
    distance[A] = 0
    v = (A, -1)

    while True:
        visited[v[0]] = True
        next_v = -1
        min_dist = inf
        next_d = -1

        for u in range(glen):
            if not visited[u]:

                if G[v[0]][u] != 0 and G[v[0]][u] != v[1] and distance[u] > distance[v[0]] + G[v[0]][u]:
                    distance[u] = distance[v[0]] + G[v[0]][u]

                if distance[u] < min_dist and G[v[0]][u] != v[1]:
                    next_v = u
                    next_d = G[v[0]][u]
                    min_dist = distance[u]

        if next_v == -1:
            return distance[B]

        v = (next_v, next_d)


G = [[0, 1, 0, 0],
     [1, 0, 1, 5],
     [0, 1, 0, 1],
     [0, 5, 1, 0]]

print(islands(G, 0, 3))


#runtests(islands)
