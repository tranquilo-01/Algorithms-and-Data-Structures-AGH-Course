from metody import naturalarray, print_list, list2tab, tab2list


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def selection_sort(first):
    # znalezc najmniejszy element i dac na poczatek
    lowest = first
    lowest_prev = prev = first
    compared = first

    flag0 = False
    while compared.next is not None:
        compared = compared.next
        if compared.val < lowest.val:
            flag0 = True
            lowest = compared
            lowest_prev = prev
        prev = prev.next

    if flag0:
        lowest_prev.next = lowest.next
        lowest.next = first
        first = lowest
        first_copy = last_sorted = first
        lowest_prev = prev = first_copy
        compared = first = lowest = first_copy.next
    else:
        first_copy = first
        last_sorted = lowest_prev = prev = first_copy
        compared = first = lowest = first_copy.next

    # teraz jak w selection sorcie dzielimy liste na nieposortowana i posortowana i wstawiamy
    # kolejne najmniejsze elementy na poczatek nieposortowanej, tylko zamiast jak w tablicy zamieniac elementy
    # tutaj przepinamy tego nodea

    while first.next is not None:

        flag = False
        while compared is not None:
            if compared.val < lowest.val:
                flag = True
                lowest = compared
                lowest_prev = prev
            compared = compared.next
            prev = prev.next

        if flag:
            lowest_prev.next = lowest.next
            lowest.next = first
            last_sorted.next = lowest

        lowest_prev = prev = last_sorted = lowest
        first = compared = lowest.next
        lowest = lowest.next

    return first_copy


def selection_sort_k_chaotic(first, k):
    # znalezc najmniejszy element i dac na poczatek
    lowest = first
    lowest_prev = prev = first
    compared = first

    flag0 = False
    i = 0
    while compared.next is not None and i < k:
        compared = compared.next
        i += 1
        if compared.val < lowest.val:
            flag0 = True
            lowest = compared
            lowest_prev = prev
        prev = prev.next

    if flag0:
        lowest_prev.next = lowest.next
        lowest.next = first
        first = lowest
        first_copy = last_sorted = first
        lowest_prev = prev = first_copy
        compared = first = lowest = first_copy.next
    else:
        first_copy = first
        last_sorted = lowest_prev = prev = first_copy
        compared = first = lowest = first_copy.next

    # teraz jak w selection sorcie dzielimy liste na nieposortowana i posortowana i wstawiamy
    # kolejne najmniejsze elementy na poczatek nieposortowanej, tylko zamiast jak w tablicy zamieniac elementy
    # tutaj przepinamy tego nodea

    while first.next is not None:
        i = 0
        flag = False
        while compared is not None and i < k:
            i += 1
            if compared.val < lowest.val:
                flag = True
                lowest = compared
                lowest_prev = prev
            compared = compared.next
            prev = prev.next

        if flag:
            lowest_prev.next = lowest.next
            lowest.next = first
            last_sorted.next = lowest

        lowest_prev = prev = last_sorted = lowest
        first = compared = lowest.next
        lowest = lowest.next

    return first_copy


tablica = [3, 4, 1, 2, 8, 7, 5, 6, 9, 11, 10, 12]
print(tablica)
tablica2 = tablica.copy()
tablica2.sort()
print(tablica2)
lista = tab2list(tablica)
print_list(lista)
p = selection_sort_k_chaotic(lista, 3)
print_list(p)
