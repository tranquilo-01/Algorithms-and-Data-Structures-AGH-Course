# # opis w onenote
# # mamy n klocków które spadaja na os liczbowa, chcemy, aby każdy klocek lezal w calosci na poprzednim,
# # klocki podane w tablicy, mamy wybrac klocki do usuniecia tak żeby zbudowac jak najwyzszy stos


# def g(T):
#     n = len(T)
#
#     # tablica na spamietywanie czy mozna zbudoeac wieze danej wysokosci
#     res = [[None for i in range(n)] for j in range(n)]
#
#     for i in range(n):
#         res[i][1] = True
#
#         for j in range(i + 1, n + 1):
#             res[i][j] = False
#
#     def f(T, i, k, res):
#         if res[i][k] is None:
#             res[i][k] = f(T, i - 1, k, res)
#             for j in range(1, i + 1):
#                 if [i][0] >= T[i - 1][0] and T[i][1] <= T[i - 1][1]:
#                     res[i][k] = res[i][k] or f(T, i - j, k - 1, res)
#         return res[i][k]
#
#    for k in range(n, 0, -1):
#        if f(T, i, k, res):
#            return k


# będziemy sprawdzac czy można zbudowac wieze wysokosci k z klockow od 0 do i


def g(T):
    n = len(T)
    res = [[0 for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        res[i][1] = True
        for j in range(i + 1, n + 1):
            res[i][j] = False

    def f(T, i, k, res):
        if res[i][k] == 0:
            res[i][k] = f(T, i - 1, k, res)
            for j in range(1, i + 1):
                if T[i][0] > T[i - j][0] and T[i][1] <= T[i - j][1]:
                    res[i][k] = res[i][k] or f(T, i - j, k - 1, res)

        return res[i][k]

    for k in range(n, 0, -1):
        if f(T, i, k, res):
            return k
