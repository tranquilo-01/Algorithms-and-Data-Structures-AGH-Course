# Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n   1. Dla każdego i     0, . . . , n   1
# znany jest zysk ci, jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać
# maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę
# zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

def cut_rek(trees, i):
    if i < 0:
        return 0

    if i == 0:
        return trees[0]

    if i == 1:
        return max(trees[0], trees[1])

    return max(cut_rek(trees, i-1), cut_rek(trees, i-2) + trees[i])


def cut_memo(trees):
    n = len(trees)
    lookup = [-1 for _ in range(n)]

    def rek(t, i):
        if i < 0:
            return 0

        if i == 0:
            return t[0]

        if i == 1:
            return max(t[0], t[1])

        if lookup[i] != -1:
            return lookup[i]

        lookup[i] = max(cut_rek(t, i - 1), cut_rek(t, i - 2) + t[i])
        return lookup[i]

    r = rek(trees, n-1)
    return r


def cut_tab(trees):
    n = len(trees)
    lookup = [-1 for i in range(n)]
    lookup[0] = trees[0]
    lookup[1] = max(trees[0], trees[1])

    for i in range(2, n):
        lookup[i] = max(lookup[i-1], lookup[i-2] + trees[i])

    return lookup[-1]


arr = [2, 1, 3, 7, 4, 2, 0, 6, 9]
print(cut_rek(arr, 8))
print(cut_memo(arr))
print(cut_tab(arr))



