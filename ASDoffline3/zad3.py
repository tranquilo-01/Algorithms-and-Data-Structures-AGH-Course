from zad3testy import runtests


def insertion_sort(tab):
    tlen = len(tab)
    for i in range(1, tlen):
        key = tab[i]

        j = i - 1
        while j > -1 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key


def bucket_sort_2(tab, a, b):
    n = len(tab) // 10
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


def SortTab(T, P):
    """znajduje zakres i sortuje bucketem, olewa rozklad"""
    minn = 10 ** 6
    maxx = 0
    for interval in P:
        if interval[0] < minn:
            minn = interval[0]
        if interval[1] > maxx:
            maxx = interval[1]

    bucket_sort_2(T, minn, maxx + 1)
    return T


runtests(SortTab)
