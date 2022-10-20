import copy
from insertion_sort import insertion_sort
from z_metody import naturalarray


# sortuje liniowo n liczb z rozkladu jednostajnego na przedziale [a, b)
# pierwsza wersja sortuje buckety a potem wypelnia tablice (wolniejsza)
def bucket_sort_1(tab, a, b):
    n = len(tab)
    buckets = [[] for _ in range(n)]

    # adding to buckets
    for el in tab:
        ind = int((el - a) / (b - a) * n)
        buckets[ind].append(el)

    # sorting buckets
    for bucket in buckets:
        insertion_sort(bucket)

    # adding to input array
    i = 0
    for bucket in buckets:
        for element in bucket:
            tab[i] = element
            i += 1


# druga wersja najpierw wypelnia tablice bucketami (niekoniecznie posortowanymi)
# a potem insertion sortuje cala tablice (szybsza)
def bucket_sort_2(tab, a, b):
    n = len(tab)
    buckets = [[] for _ in range(n)]

    # adding to buckets
    for el in tab:
        ind = int((el - a) / (b - a) * n)
        buckets[ind].append(el)

    # adding to input array
    i = 0
    for bucket in buckets:
        for element in bucket:
            tab[i] = element
            i += 1

    insertion_sort(tab)


arr1 = naturalarray(10 ** 6, 0, 10 ** 3 - 1)
arr2 = copy.deepcopy(arr1)
bucket_sort_1(arr1, 0, 10 ** 3)
bucket_sort_2(arr2, 0, 10 ** 3)
