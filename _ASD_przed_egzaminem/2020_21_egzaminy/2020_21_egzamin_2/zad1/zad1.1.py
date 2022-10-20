from zad1testy import runtests
from collections import deque


# Całkowita złożoność czasowa: O(nlogn)

def binary_search(A, val, side):
    p = 0
    r = len(A) - 1
    last_id = None  # Tutaj zapisujemy pierwsze wystąpienie w tablicy przedziału o żądanej włsności
    while p <= r:
        q = (p + r) // 2
        if A[q][0][side] == val:
            last_id = q
        if A[q][0][side] >= val:
            r = q - 1
        else:
            p = q + 1
    return last_id


def wave_processing(T, visits, x, y, side):
    n = len(T)
    Q = deque()  # Kolejka
    for i in range(n):
        if T[i][0][side] == x:
            Q.append(T[i])
            visits[T[i][1]] = True
    while Q:
        x = Q.popleft()
        # Wyszukujemy binarnie pierwszy przedział na liście, którego początek lub koniec równy jest odp.
        # końcowi lub początkowi przedziału x. Staje się on "reprezentantem" grupy przedziałów mających
        # wspólny koniec lub początek, więc sprawdzając, czy reprezentant został odwiedzony, sprawdzamy
        # de facto czy odwiedziliśmy wszystkie przedziały z grupy (Sprawdzenie staje się O(1)).
        first = binary_search(T, x[0][(side + 1) % 2], side)
        if first is None or visits[T[first][1]]:
            continue
        for i in range(first, n):  # Dodajemy do kolejki "falami" wszystkie nowo dostępne przedziały
            if T[i][0][side] != x[0][(side + 1) % 2]:
                break
            Q.append(T[i])
            visits[T[i][1]] = True


def intuse(A, x, y):
    n = len(A)
    L = []
    R = []
    for i in range(n):
        if A[i][0] >= x and A[i][1] <= y:
            L.append((A[i], i))
    L.sort(key=lambda x: x[0])  # Tablica L służąca do badania lewych krańców przedziałów
    for i in range(len(L)):
        R.append((L[i][0], i, L[i][1]))  # Drugi element krotki to pozycja elementu w równoległej tablicy L
        L[i] = (L[i][0], i, L[i][1])
    R.sort(key=lambda x: x[0][1])  # Tablica R służąca do badania prawych krańców przedziałów
    # Dwa sortowania: O(nlogn)
    visits_from_beg = [False for i in range(len(L))]  # Przedziały osiągalne z tych o początku x
    visits_from_end = [False for i in range(len(R))]  # Przedziały osiągalne z tych o końcu w y
    wave_processing(L, visits_from_beg, x, y, 0)  # Niejawny BFS startując z przedziałów o początku w x
    wave_processing(R, visits_from_end, y, x, 1)  # Niejawny BFS startując z przedziałów o końcu w y
    # Dwa wywołania wave_processing: O(nlogn) (potencjalnie n wyszukań binarnych)
    result = []
    for i in range(len(L)):
        # Jeżeli przedział jest osiągaly zarówno z początku x jak i końca y, to jest przydatny
        if visits_from_beg[i] and visits_from_end[i]:
            result.append(L[i][2])
    # Liniowe przejście: O(n)
    return result


# Przykładowe wywołanie dla I = [(1, 2), (5, 6), (4, 5), (1, 3), (3, 5), (2, 5) oraz x = 1, y = 6:

# wave_processing nr 1: start -> (1,2), (1, 3) -> (2, 5), (3, 5) -> (5, 6) -> end

# wave_processing nr 2: end -> (5, 6) -> (2, 5), (3, 5), (4, 5) -> (1, 2), (1, 3) -> start

# Przedział (4, 5) występuje w wyszukiwaniu od końca, ale nie ma go w wyszukiwaniu od początku,
# więc nie należy do rozwiązania.

runtests(intuse)
