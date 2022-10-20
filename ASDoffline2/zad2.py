from zad2testy import runtests


# Krzysztof Dziechciarz
# Opis:
# - tworze tablice intervals_sorted dwa razy dluzsza zawierajaca tablice o indeksach:
# [poziom_zdarzenia, id_przedzialu, typ_zdarzenia(otwarcie/zamkniece)]
# - tworze tablice depth_count, w ktorej bede przechowywyal glebokosc kazdzego przedzialu pod indeksem odpowiadajacym id przedzialu
# -przechodze dwa razy liniowo po intervals_sorted i dla kazdego przedzialu zapisuje w depth_count wartosc:
# (ilosc przedzialow) - (ilosc przedzialow otwartych na lewo od otwarcia danego przedzialu) - (ilosc przedzialow zamknietych na prawo od zamkniecia) - 1
# - w ten sposob mam w deph_count zanizone wartosci glebokosci dla przedzialow zawierajacych sie w innych
# i poprawna wartosc glebokosci dla przedzialow nie zawierajacych sie w innych
# - przechodze liniowo po depth_count aby znalezc najwieksza glebokosc


def quicksort(tab):
    st = [(0, len(tab) - 1)]

    while len(st) > 0:
        p, r = st.pop()

        if p < r:
            q = partition(tab, p, r)
            st.append((p, q - 1))
            st.append((q + 1, r))


def partition(tab, p, r):
    i = p - 1
    pivot = tab[r][0]
    for j in range(p, r):
        if tab[j][0] <= pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    i += 1
    tab[i], tab[r] = tab[r], tab[i]
    return i


def depth(intervals):
    intlen = len(intervals)
    sortlen = intlen * 2
    intervals_sorted = []
    for el in range(intlen):
        intervals_sorted.append((intervals[el][0], el, 0))  # 0 for start of the interval
        intervals_sorted.append((intervals[el][1], el, 1))  # 1 for end of the interval

    quicksort(intervals_sorted)

    old_starts = 0
    old_ends = 0
    starts = 0
    ends = 0
    e = 0
    depth_count = [0 for _ in range(intlen)]

    while e < sortlen:
        point = intervals_sorted[e][0]
        reference = point
        ce = e
        while point == reference:
            if intervals_sorted[e][2] == 0:
                starts += 1
                e += 1
            elif intervals_sorted[e][2] == 1:
                e += 1
            if e == sortlen:
                break
            point = intervals_sorted[e][0]
        while ce < e:
            if intervals_sorted[ce][2] == 0:
                depth_count[intervals_sorted[ce][1]] += intlen - old_starts - 1
            ce += 1
        old_starts = starts

    e -= 1
    maxx = 0
    while e > -1:
        point = intervals_sorted[e][0]
        reference = point
        ce = e
        while point == reference:
            if intervals_sorted[e][2] == 1:
                ends += 1
                e -= 1
            elif intervals_sorted[e][2] == 0:
                e -= 1
            if e == -1:
                break
            point = intervals_sorted[e][0]
        while ce > e:
            if intervals_sorted[ce][2] == 1:
                depth_count[intervals_sorted[ce][1]] += -old_ends
                if depth_count[intervals_sorted[ce][1]] > maxx:
                    maxx = depth_count[intervals_sorted[ce][1]]
            ce -= 1
        old_ends = ends

    return maxx


runtests(depth)
