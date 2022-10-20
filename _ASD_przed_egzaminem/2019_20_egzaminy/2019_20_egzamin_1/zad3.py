from zad3testy import runtests
import math


# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x
# , gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
# Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
# zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej.
# Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową.

# pomysl jest taki zeby oblozyc wszystko ln o podstawie a - wtedy dostajemy x
# nastepnie soertujemy po x bucketsortem, bo sa rozlozone jednosstajnie
# zlozonosc O(n)
def selection_sort(tab):
    n = len(tab)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if tab[j] < tab[i]:
                idx = j
        tab[i], tab[idx] = tab[idx], tab[i]


def fast_sort(tab, a):
    n = len(tab)
    buckets = [[] for _ in range(n)]
    for el in tab:
        idx = int(math.log(el, a) * n)
        buckets[idx].append(el)

    for bucket in buckets:
        if len(bucket) > 1:
            selection_sort(bucket)

    srtd = [-1 for _ in range(n)]
    i = 0

    for bucket in buckets:
        for element in bucket:
            srtd[i] = element
            i += 1
    return srtd


runtests(fast_sort)
