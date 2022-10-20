# Składanie dwóch posortowanych list
from z_metody import tab2list, list2tab, print_list


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge(first1, first2):
    if first1 is None:
        return first2
    if first2 is None:
        return first1
    if first1.val > first2.val:
        first1, first2 = first2, first1
    First = first1
    first1 = first1.next
    p = First
    p.next = None
    val1 = first1
    val2 = first2
    while val1 is not None and val2 is not None:
        if val1.val > val2.val:
            first1, first2 = first2, first1
        p.next = first1
        first1 = first1.next
        p = p.next
        p.next = None
    if val1 is None:
        p.next = val2
    elif val2 is None:
        p.next = val1
    return First


# MergeSort na seriach naturalnych (na linked listach ze wskaźnikami na pierwszy element w serii)
# 1, 2, 5, 3, 6, 4 ,2, 3, 4, 1, 5
# (1, 2, 5) (3, 6) (4) (2, 3, 4) (1, 5)
#          \/         \/            |
#            \        /             |
#              \    /               |
#                \/                 |
#                 |_________________|
#                         |
def merge_ll(f1, f2):
    if f1 is None:
        return f2
    if f2 is None:
        return f1

    if f1.val < f2.val:
        final_first = f1
        f1 = f1.next
    else:
        final_first = f2
        f2 = f2.next

    f = final_first

    while f1 is not None and f2 is not None:
        if f1.val <= f2.val:
            f.next = f1
            f1 = f1.next
            f = f.next
        else:
            f.next = f2
            f2 = f2.next
            f = f.next

    while f1 is not None:
        f.next = f1
        f1 = f1.next
        f = f.next
    while f2 is not None:
        f.next = f2
        f2 = f2.next
        f = f.next

    return final_first


def merge_sort(first):
    # merge sort korzystajacy z serii naturalnych
    # na poczatku kopletujemy tablice ze wskaznikami na poczatki serii:
    heads = [first]
    if first.next is None:
        return first
    curr = first.next
    while curr is not None:
        if curr.val >= first.val:
            first = first.next
            curr = curr.next
        else:
            heads.append(curr)
            first.next = None
            first = curr
            curr = curr.next

    # potem scalamy wszystkie serie:
    while len(heads) > 1:
        while len(heads) > 1:
            heads2 = []
            merged = merge_ll(heads[0], heads[1])
            heads2.append(merged)
            heads = heads[2:]
            heads2.extend(heads)
            heads = heads2
    return heads[0]


# tab1 = [1, 5, 8]
# tab2 = [2, 4, 9]
# t1 = tab2list(tab1)
# t2 = tab2list(tab2)
#
# m = merge_ll(t1, t2)
# print_list(m)


# Zliczanie wszystkich inwersji (np. dla 1, 3, 2, 7, 5, 6 jest inwersja dla 3 i 2, 7 i 5, 7 i 6), czyli sytuacje gdy wartość na większym indeksie jest mniejsza niz ta na mniejszym)
# MODYFIKACJE DO FUNKCJI MERGE:
# if L1.val > L2.val:
#   merged.append(L2)
#   inwersje += 1
# else:
#   merged.append(L1)
# Dodajemy licznik inwersji w funkcji merge gdy zmienia się wskaźnik na mniejszą wartosć i zliczamy wtedy
# inwersję tylko najpierw musimy liste podzielic na serie naturalne albo ogolnie tak jak w MergeSorcie (chyba) niby mozna dowolnie podzielic ale idk co miał na myśli

# Mamy prostokątne pojemniki z woda na płaszczyźnie (mozemy wybobrazać to sobie jako pojemniki w trzech wymiarach gdzie kazdy ma trzeci wymiar jako jedna jednostka),
# które na siebie nie zachodzą i kazdy z kazdym jest połączony rurami i woda między nimi swobodnie przepływa. Kazdy pojemnik jest zapisany jako współrzędne lewego górnego wierzchoła,
# szerokość i wysokość. Pojemniki wypełniają sie od dołu i zastanawiamy się jak policzyć jak najwydajniej ile pojemników jest w pełni zalanych. W danych mamy ilość wlanej do układu wody.

#   ____            _______
#  |    |          |       |
#  |____|          |       |
#    |             |_______|
#    |    ___          |
#    |---|   |---------|
#        |   |       __|___
#        |   |------|______|
#        |___|

# Idziemy co 1 zdarzenie (poczatek albo koniec zbiornika) najpierw je sortując (idąc w górę) i trzymamy informacje o aktywnych (zalewanych) zbiornikach oraz o tych juz zalanych
# az nasza wykorzystana na tej wysokosci objetosc nie osiagnie wartosci większej od nalanej wody (wtedy rozwazamy stan z poprzedniego zdarzenia) lub gdy się zrówna.
# Gdy znajdziemy poziom wody to zliczamy wszystkie w pelni zalane zbiorniki. Liniowo logarytmiczna zlozonosc

# A - tablica z n liczbami
# Czy istnieje x (lider ciągu) taki, ze wystepuje w A co najmniej n/2 razy. (O(n)!)


def scalanie(p1, p2):
    if p1.val < p2.val:
        s = p1
        p1 = p1.next
        s.next = None
    else:
        s = p2
        p2 = p2.next
        s.next = None
    sp = s
    while p1 is not None:
        if p2 is None:
            sp.next = p1
            break
        if p1.val < p2.val:
            sp.next = p1
            p1 = p1.next
            sp = sp.next
        else:
            sp.next = p2
            p2 = p2.next
            sp = sp.next
    sp.next = p2
    p2 = None
    while sp.next is not None:
        sp = sp.next
    return s, sp


def podziel(p):
    new = p
    while p is not None:
        if p.next.val < p.val:
            tmp = p
            p = p.next
            tmp.next = None
            return new
        p = p.next


def mergesort(p):
    head = p
    while True:
        n = 0
        tail = head
        while p.next is not None:
            s1 = podziel(p)
            n += 1
            if p.next is None:
                tail.next = s1
            else:
                s2 = podziel(p)
                n += 1
                m_head, m_tail = scalanie(s1, s2)
                tail.next = m_head
                tail = m_tail
        p = head


arr = [2, 1, 3, 7, 4, 2, 0, 6, 9]
p = tab2list(arr)
print_list(p)
p = MergeSort(p)
print_list(p)
