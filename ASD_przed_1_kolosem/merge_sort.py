def merge_sort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2

        left = []
        for l in range(mid):
            left.append(tab[l])

        right = []
        for r in range(mid, len(tab)):
            right.append(tab[r])

        merge_sort(left)
        merge_sort(right)

        # merging
        l = r = i = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                tab[i] = left[l]
                l += 1
            else:
                tab[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            tab[i] = left[l]
            l += 1
            i += 1
        while r < len(right):
            tab[i] = right[r]
            r += 1
            i += 1


tab = [2, 1, 3, 7, 4, 2, 0, 6, 9]
merge_sort(tab)
print(tab)
