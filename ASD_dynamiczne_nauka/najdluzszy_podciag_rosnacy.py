# O(n^2)

# maxj obslugluje found_lis, ktore sluzy do zwracania tablicy, z ktorej mozna potem odczytac lis
# opis na wykladzie

def lis(sequence):
    n = len(sequence)
    tmp = [1 for _ in range(n)]
    found_lis = [-1 for i in range(n)]
    tmp[0] = 1

    for i in range(1, n):
        maxlen = 1
        maxj = -1
        for j in range(i):
            if sequence[j] < sequence[i] and tmp[j] >= maxlen:
                maxlen = tmp[j] + 1
                maxj = j
        tmp[i] = maxlen
        found_lis[i] = maxj

    return max(tmp), found_lis


def print_seq(sequence, found, i):
    if found[i] != -1:
        print_seq(sequence, found, found[i])
    print(sequence[i], end=" ")


seq = [2, 1, 3, 7, 4, 2, 0, 6, 9]
res, tab = lis(seq)
print(res)
print_seq(seq, tab, len(tab) - 1)
