# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową

# do drugiej tablicy o dl tablicy wejsciowej bedziemy zapisywac "ladnosc" liczby przedstawiona wg wzoru :
# 11*(liczba cyfr jednokrotnych)-(liczba cyfr wielokrotnych)
# potem przy pomocy counting sorta (+ radix sorta) liniowo posortujemy tablice wejsciowa na podstawie tablicy pomocniczej
# zlozonosc O(n)

def build_prettiness_array(tab):
    arr = [200] * len(tab)  # zaczynamy od 200 bo wtedy nie ma ujemnych i wszystkie sa 3-cyfrowe
    i = 0
    for el in tab:
        counter = [0] * 10
        while el > 0:
            counter[el % 10] += 1
            el //= 10
        for c in counter:
            if c == 1:
                arr[i] += 11
            elif c > 1:
                arr[i] -= 1
        i += 1

    return arr


def radix_sort(numbers, prettiness_array):
    nlen = len(numbers)
    for i in range(3):
        # wszystko ponizej to counting w radixie
        counts = [0] * 10
        final_prettiness = [0] * nlen
        final_numbers = [0] * nlen
        for n in prettiness_array:
            counts[getdigit(n, i)] += 1
        for j in range(1, 10):
            counts[j] += counts[j - 1]
        for k in range(nlen - 1, -1, -1):
            final_prettiness[counts[getdigit(prettiness_array[k], i)] - 1] = prettiness_array[k]
            final_numbers[counts[getdigit(prettiness_array[k], i)] - 1] = numbers[k]
            counts[getdigit(prettiness_array[k], i)] -= 1
        for k in range(nlen):
            prettiness_array[k] = final_prettiness[k]
            numbers[k] = final_numbers[k]


def getdigit(number, digit):
    return number // (10 ** digit) % 10


lista = [123, 455, 1266, 114577, 2344, 67333, 1234567890, 11223344556677889900]
print(lista)
pa = (build_prettiness_array(lista))
print(pa)
radix_sort(lista, pa)
print(pa)
print(lista)
