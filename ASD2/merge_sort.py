def merge_sort(tab, p, k):
    if k - p == 1:
        return 0

    s = (k + p) // 2

    merge_sort(tab, p, s)
    merge_sort(tab, s, k)
    merge(tab, p, s, k)


def merge(tab, p, s, k):
    tmp = [0] * (k - p)

    l = p
    j = 0
    r = s

    while l < s and r < k:
        if tab[l] <= tab[r]:
            tmp[j] = tab[l]
            l += 1
        else:
            tmp[j] = tab[r]
            r += 1
        j += 1

    while l < s:
        tmp[j] = tab[l]
        l += 1
        j += 1
    while r < k:
        tmp[j] = tab[r]
        r += 1
        j += 1

    x = 0
    for i in range(p, k):
        tab[i] = tmp[x]
        x += 1


arr = [2, 1, 3, 7, 4, 2, 0, 6, 9, 5, 9876, 8, 90]
merge_sort(arr, 0, len(arr))





