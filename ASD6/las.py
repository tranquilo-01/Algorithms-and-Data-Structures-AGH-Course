# opis w one note
# na każdej liczbie na osi liczbowej rosnie drzewo, ze sciecia kazdego
# drzewa otrzymujemy zysk, nie można sciac sasiadujacych drzew, mamy mieć najwiekszy zysk

def las(C, n):
    # tablica na spamietywanie
    T = [-1 for i in range(n)]

    # warunki trywialne
    T[0] = C[0]
    T[1] = max(C[0], C[1])

    # reszta rekurencyjnie
    # def f(C, i):
    #     if T[i] == -1:
    #         T[i] = max(f(C, i-1), f(C, i-2) + C[i])
    #     return T[i]
    #
    #
    # return f(C, n-1)

    # # inaczej
    for i in range(2, n):
        T[i] = max(T[i-1], T[i-2] + C[i])

    print(T)
    return T[n-1]


arr = [2, 1, 3, 7, 4, 2, 0, 6, 9]
print(las(arr, len(arr)))