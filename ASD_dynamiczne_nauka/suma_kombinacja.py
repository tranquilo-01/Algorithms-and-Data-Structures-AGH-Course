# Given 3 numbers {1, 3, 5}, we need to tell
# the total number of ways we can form a number 'N'
# using the sum of the given three numbers.
# (allowing repetitions and different arrangements).

# rozwiazanie dla n (w zbiorze zawsze jest jedynka):

# aby osiagnac ilosc sum od n nalezy zsumowac wszystkie mozliwosci dla n - {el}, gdzie el jest elementem ze zbioru

def sum_numbers_exponential(sett, suma):
    def sne(sett, curr, suma):
        if curr == 0:
            return 1

        i = 0

        for el in sett:
            if curr - el >= 0:
                i += sne(sett, curr-el, suma)
        return i

    return sne(sett, suma, suma)


def sum_numbers_polynomial(sett, suma):
    tab = [-1 for _ in range(suma)]

    def snp(sett, curr, suma):
        if curr == 0:
            return 1

        i = 0

        if tab[curr-1] == -1:
            for el in sett:
                if curr - el >= 0:
                    i += snp(sett, curr-el, suma)
                    tab[curr-1] = i
        return tab[curr-1]

    return snp(sett, suma, suma)


print(sum_numbers_polynomial([1, 3, 5], 35))

