from math import inf
from queue import PriorityQueue

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


def dijkstra(G, v, t):
    n = len(G)
    d = [[inf, inf, inf] for _ in range(n)]
    d[v][0] = 0
    d[v][1] = 0
    d[v][2] = 0
    K = PriorityQueue()

    for i in range(n):
        if G[v][i] != 0:
            if G[v][i] == 1:
                x = 1
                y = 0
            elif G[v][i] == 5:
                x = 5
                y = 1
            else:
                x = 8
                y = 2
            G[v][i] = 0
            G[i][v] = 0
            if d[i][y] > x:
                d[i][y] = x
                K.put((d[i][y], i, x))

    while not K.empty():
        u = K.get()
        if u[1] == t:
            return u[0]
        for v in range(n):
            # robie teraz tą notatke na szybko (mogę pisać głupoty)
            # x to chyba to to co dodam do dotychczasowego kosztu podróży
            # y to indeks pod którym zapisze ten koszt
            # (każdy wierzchołek ma tablice 3 elem. w zaleznosci czy docieram tam samolotem, promem czy mostem)
            # do kolejki przekazuje krotke (koszt, wierzchołek, jak tam dotarłam (wartosc x to okresla))
            # G[u[1]][v] != u[2] warunek zeby nie isc do nastepnego wiercholka w taki sam spsob
            if G[u[1]][v] != 0 and G[u[1]][v] != u[2]:
                if G[u[1]][v] == 1:
                    x = 1
                    y = 0
                elif G[u[1]][v] == 5:
                    x = 5
                    y = 1
                else:
                    x = 8
                    y = 2
                G[u[1]][v] = 0
                G[v][u[1]] = 0
                if d[v][y] > u[0] + x:
                    d[v][y] = u[0] + x
                    K.put((d[v][y], v, x))
    return None


def islands(G, A, B):
    return dijkstra(G, A, B)


runtests(islands)
