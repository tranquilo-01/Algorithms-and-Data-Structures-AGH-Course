from heap_sort_array import heap_sort, heap_sort_k_chaotic, build_heap_k_chaotic, build_heap
from random import randrange
import copy
import time

MY_seed = randrange(100)
MY_a = 134775813
MY_c = 1
MY_modulus = 2 ** 32


def MY_random():
    global MY_seed, MY_a, MY_c, MY_modulus
    MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
    return MY_seed


def gentest(k, n, maxint):
    l = [MY_random() % maxint for i in range(n)]
    l = sorted(l)
    pos = [i for i in range(n)]

    for i in range(n):
        if pos[i] != i: continue

        j = i + (MY_random() % (k + 1))
        if n > j == pos[j]:
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
            tmp = pos[i]
            pos[i] = pos[j]
            pos[j] = tmp

    arg = (l, k)
    hint = sorted(l)
    return arg, hint


k = 3
n = 10
maxint = 100
dane = gentest(k, n, maxint)
tablica = dane[0][0]
# tablica2 = copy.deepcopy(tablica)
# tablica.reverse()
# posortowana = dane[1]
print(tablica)
# # print(posortowana)
#
# ts1 = time.time()
# heap_sort_k_chaotic(tablica, k)
# te1 = time.time() - ts1
#
# ts2 = time.time()
# heap_sort(tablica2)
# te2 = time.time() - ts2
#
# # print(tablica)
# # print(tablica2)
# print(tablica == tablica2)
# print("chaotic", te1)
# print("heap", te2)
# tablica.reverse()
# print(tablica)
# build_heap(tablica)
# print(tablica)
