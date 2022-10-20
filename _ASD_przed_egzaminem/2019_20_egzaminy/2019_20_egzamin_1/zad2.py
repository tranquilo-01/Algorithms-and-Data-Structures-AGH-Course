from math import inf

from zad2testy import runtests


# Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
# być zarówno dodatnie jak i ujemne):
# n1 + n2 + ... + nk
# Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
# kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
# dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
# najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
# wybiera kolejność dodawań.
# Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie;
# zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość
# bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań. Na przykład dla tablicy
# wejściowej:
# [1,−5, 2]
# funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku


def opt_sum(tab):
    n = len(tab)
    lookup = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        lookup[i][i] = tab[i]

    def f1(a, b):
        if lookup[a][b] != -1:
            return lookup[a][b]

        if a + 1 == b:
            lookup[a][b] = abs(tab[a] + tab[b])
            return lookup[a][b]

        lookup[a][b] = max(abs(sum(tab[a:b + 1])), min(f1(a + 1, b), f1(a, b - 1)))
        return lookup[a][b]

    result = f1(0, n - 1)
    return result

runtests(opt_sum)

print(opt_sum([1, -5, 2]))
