# sorting an array filled with numbers from 0 to k-1 in linear time

def counting_sort(tab, k):
    n = len(tab)
    counts = [0] * k
    srtd = [0] * n

    # counting
    for x in tab:
        counts[x] += 1

    # cumulating
    for i in range(1, k):
        counts[i] += counts[i - 1]

    # sorting
    for i in range(n-1, -1, -1):
        srtd[counts[tab[i]] - 1] = tab[i]
        counts[tab[i]] -= 1

    # copying from srtd to input tab
    for i in range(n):
        tab[i] = srtd[i]


