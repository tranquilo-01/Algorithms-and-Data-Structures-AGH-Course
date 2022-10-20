# Mówimy, ze wierzchołek t w grafie skierowanym jest uniwersalnym ujsciem, jesli
# (a) z kazdego innego wierzchołka v istnieje krawedz z v do t, oraz
# (b) nie istnieje zadna krawedz wychodzaca z t.
# 1. Podac algorytm znajdujacy uniwersalne ujscie (jesli istnieje) przy reprezentacji macierzowej (O(n2)).
# 2. Pokazac, ze ten problem mozna rozwiazac w czasie O(n) w reprezentacji macierzowej

# reprezentacja macierzowa
# O(v^2)
# liczymy ile krawedzi wchodzi do kazdego wierzcholka i ile z niego wychodzi
# do uniwersalnego ujscia wchodza wszystkie a nie wychodzi zadna

# O(v)
# w kolumnie uniwersalniego ujscia powinny byc same zera poza [u][u], a w wierszu same 1
# startujemy w [0][0] jesli w komorce mamy 0 to idzeimy w prawo a jesli 1 to w dol
# jesli wyjdziemy za macierz z prawej strony to sprawdzamy czy w wierszu w ktorym wyszlismy sa same 0


