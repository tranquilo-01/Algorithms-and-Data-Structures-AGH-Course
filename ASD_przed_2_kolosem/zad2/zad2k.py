from zad2ktesty import runtests


def palindrom(S):
    slen = len(S)
    lookup = [[False for _ in range(slen)] for _ in range(slen)]
    ind = [-1, -1]

    for i in range(slen - 1):
        lookup[i][i] = True
        if S[i] == S[i + 1]:
            lookup[i][i + 1] = True
            ind = [i, i + 1]
    lookup[slen - 1][slen - 1] = True

    maxx = 2

    for i in range(slen, -1, -1):
        for j in range(i + 1, slen):
            if lookup[i + 1][j - 1] and S[i] == S[j]:
                lookup[i][j] = True
                if j - i + 1 > maxx:
                    maxx = j - i + 1
                    ind = [i, j]

    return S[ind[0]: ind[1] + 1]


runtests(palindrom)
# print(palindrom("abaaabaaba"))
