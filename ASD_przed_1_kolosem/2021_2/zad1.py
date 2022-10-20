# Marcel Duda
# Zaciągam k+1 elementów z listy i kładę je na stos o wielkości 8B*(k+1) STOS - HEAP, NIE STACK
# (złożoność pamięciowa dla dużych n w porównaniu z k można powiedzieć że w miejscu)
# za każdym razem ściągam ze stosu najmniejszy element i kładę na
# niego następny naprawiając stos w log(k) złożoności a jako że robię to dla n elementów to złożoność całkowita algorytmu jest n*log(k+1)
# Jeśli lista jest k chaotyczna to najmniejszy element będzie najdalej od początku o maksymalnie k
# dlatego wystarczy dla pierwszego miejsca zbudować kopiec k elementowy a następnie wykorzystywać go do następnej
# pozycji aż do momentu gdzie z listy zdejmiemy n - k elementów i wtedy trzeba opróżnić kopiec i go naprawiać
# dla k = n zachowuje się jak heapsort a dla każdego mniejszego jest niższa złożoność


# MOJ POMYSL - MOZNA TAK SAMO ALE ZROBIC SOBIE KLASE MIN_HEAP KTORA TO WSZYSTKO BY OBSLUGIWALA
# (TWORZENIE, DODAWANIE KOLEJNEGO NODE, ZWRACANIE NAJWIEKSZEGO)

from zad1testy import Node, runtests


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heapify(t, i):
    p = (i - 1) // 2
    min_ind = i
    if (p >= 0) and (t[p].val > t[i].val):
        min_ind = p
    if min_ind != i:
        t[i], t[min_ind] = t[min_ind], t[i]
        heapify(t, min_ind)


def heapifyg(t, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    min_ind = i
    if l < n and t[l].val < t[min_ind].val:
        min_ind = l
    if r < n and t[r].val < t[min_ind].val:
        min_ind = r
    if min_ind != i:
        t[i], t[min_ind] = t[min_ind], t[i]
        heapifyg(t, n, min_ind)


def build_heap(p, t, k):
    d = 0
    while p is not None and d < k:
        t[d] = p
        p = p.next
        heapify(t, d)
        d += 1
    return p


def SortH(p, k):
    # budowanie kopca
    t = [None for i in range(k + 1)]
    p = build_heap(p, t, k + 1)
    s = t[0]
    s.next = None
    scurr = s

    # ? - chyba jakby kopiec nie caly sie zbudowal to przechodzenie do konca
    while t[k] is None:
        k -= 1

    # wlasciwe sortowanie
    while p is not None:
        t[0] = p
        p = p.next
        heapifyg(t, k + 1, 0)
        scurr.next = t[0]
        scurr = scurr.next
        scurr.next = None
    # ?
    t[k], t[0] = t[0], t[k]
    heapifyg(t, k, 0)

    # sortowanie ostatnich k elementow
    for i in range(k - 1, -1, -1):
        scurr.next = t[0]
        scurr = scurr.next
        t[i], t[0] = t[0], t[i]
        heapifyg(t, i, 0)
    scurr.next = None
    return s


runtests(SortH)
