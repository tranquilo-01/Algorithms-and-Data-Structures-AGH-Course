def naive_rek(str1, l1, str2, l2):
    if l1 < 0 or l2 < 0:
        return 0
    if str1[l1] == str2[l2]:
        return naive_rek(str1, l1 - 1, str2, l2 - 1) + 1
    else:
        return max(naive_rek(str1, l1 - 1, str2, l2), naive_rek(str1, l1, str2, l2 - 1))


def memoization(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    lookup = [[-1 for _ in range(l2)] for _ in range(l1)]

    def rek(s1, curr_1, s2, curr_2):
        if curr_1 < 0 or curr_2 < 0:
            return 0

        if lookup[curr_1][curr_2] != -1:
            return lookup[curr_1][curr_2]

        if s1[curr_1] == s2[curr_2]:
            lookup[curr_1][curr_2] = rek(s1, curr_1 - 1, s2, curr_2 - 1) + 1
            return lookup[curr_1][curr_2]

        else:
            lookup[curr_1][curr_2] = max(rek(s1, curr_1 - 1, s2, curr_2), rek(s1, curr_1, s2, curr_2 - 1))
            return lookup[curr_1][curr_2]

    return rek(str1, l1 - 1, str2, l2 - 1)




def tabulation(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    lookup = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(l1+1):
        lookup[i][0] = 0

    for i in range(l2+1):
        lookup[0][i] = 0

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i-1][j], lookup[i][j-1])

    for row in lookup:
        print(row)
    return lookup[-1][-1]


# print(memoization("KACSEDNXCYMOZC", "JAFSLDSAIJZDSC"))
# print(naive_rek("KACSEDNXCYMOZC", 13, "JAFSLDSAIJZDSC", 13))
print(tabulation("ABCD", "ZCDF"))

