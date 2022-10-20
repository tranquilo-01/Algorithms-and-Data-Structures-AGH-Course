from zad1ktesty import runtests


# Dany jest ciąg binarny tj. zer oraz jedynek S. Proszę znaleźć taki SPÓJNY fragment tego ciągu,
# w którym różnica pomiędzy ilością zer, a jedynek, będzie jak największa. Jeżeli w ciągu występują same jedynki,
# należy założyć, że rozwiązaniem jest -1


def roznica(S):
    slen = len(S)
    lookup = [[0 for _ in range(slen)] for _ in range(slen)]

    for i in range(slen):
        if S[i] == '1':
            lookup[i][i] = -1
        elif S[i] == '0':
            lookup[i][i] = 1

    maxx = -1
    for i in range(slen):
        for j in range(i + 1, slen):
            if S[j] == '1':
                lookup[i][j] = lookup[i][j - 1] - 1
                maxx = max(maxx, lookup[i][j])
            else:
                lookup[i][j] = lookup[i][j - 1] + 1
                maxx = max(maxx, lookup[i][j])

    return maxx


runtests(roznica)
