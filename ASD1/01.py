# chyba 6

# dana jest tablica wielkosci n z wartosciami od 0 do m, znalezc najmniejsza wartosc ktorej nie ma w tablicy

# szukamy binarnie pierwszego elementu ktory nie jest rowny swojemu indeksowi

def zad(tab):
    l = 0
    p = len(tab) - 1
    while l <= p:
        s = int((l + p) / 2)
        if tab[s] == s:
            l = s + 1
        else:
            p = s - 1
    return l


tablica = [0, 1, 2, 3, 5, 7, 11, 13, 17]
print(zad(tablica))
