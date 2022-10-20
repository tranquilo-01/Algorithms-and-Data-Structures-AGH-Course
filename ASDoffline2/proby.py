def partition(tab, l, r):
    i = l - 1
    for j in range(l, r):
        if tab[j][0] <= tab[r][0]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]

    return i + 1


def quick_sort(tab, l, r):
    if l < r:
        q = partition(tab, l, r)
        quick_sort(tab, l, q - 1)
        quick_sort(tab, q + 1, r)


def split(tab):
    # funkcja rozdziela tablice przedzialow na tablice o zawartosci (wartosc(otwarcia lub zamkniecia), id przedzialu)
    tlen = len(tab)
    intervals = [(0, 0) for _ in range(tlen * 2)]
    for i in range(tlen):
        j = i * 2
        intervals[j] = (tab[i][0], i)
        intervals[j + 1] = (tab[i][1], i)
    return intervals


def quadratic(tab, quant):
    #   MOZNA TO JAKOS ZMODYFIKOWAC NA DWUWYMIAROWA I POWINNO BYC GIT CHOCIAZ W CHUJ PAMIECI???
    qlen = len(quant)
    tlen = len(tab)
    maxx = 0
    results = [0 for i in range(qlen)]
    for idd in range(qlen):
        counting = [0 for _ in range(qlen)]
        i = 0
        while tab[i][1] != idd:
            i += 1
        i += 1
        while not tab[i][1] == idd:
            counting[tab[i][1]] += 1
            if counting[tab[i][1]] == 2:
                results[idd] += 1
                maxx = max(maxx, results[idd])
            i += 1
        while not tab[i][1] == idd:
            counting[tab[i][1]] += 1
            if counting[tab[i][1]] == 2:
                results[idd] += 1
                maxx = max(maxx, results[idd])
            i += 1
    return maxx


def max_interval_count(intervals):
    interval_sorted = []
    for idx, interval in enumerate(intervals):
        s, e = interval
        l = e - s
        interval_sorted.append([s, idx, 0, l])  # 0 for start
        interval_sorted.append([e, idx, 1, l])  # 1 for end
    interval_sorted.sort(key=lambda x: (x[0], -x[2], x[3]))

    # print(interval_sorted)

    number_of_starts = 0
    number_of_ends = 0
    maxx = 0

    overlap_count = {}
    for event in interval_sorted:
        _, idx, start_end, __ = event
        if start_end == 0:  # start event
            # subtract all the ending before it
            overlap_count[idx] = - number_of_ends
            number_of_starts += 1
        else:  # end event
            overlap_count[idx] += (number_of_ends)
            if overlap_count[idx] > maxx:
                maxx = overlap_count[idx]
            number_of_ends += 1
    return maxx
    # print(overlap_count)

    #
    # # to juz jest do zwracania
    # ans_idx = -1
    # max_over_count = 0
    # min_len_interval = 99999999999
    # for idx, overl_cnt in overlap_count.items():
    #     if overl_cnt > max_over_count:
    #         ans_idx = idx
    #         max_over_count = overl_cnt
    #     elif overl_cnt == max_over_count and overl_cnt > 0 and (intervals[idx][1] - intervals[idx][0] + 1) < min_len_interval:
    #         min_len_interval = (intervals[idx][1] - intervals[idx][0] + 1)
    #         ans_idx = idx
    # if ans_idx == -1:
    #     return ans_idx
    # return intervals[ans_idx]


def max_interval_depth(intervals):
    intervals_sorted = []
    intlen = len(intervals)
    for el in range(intlen):
        intervals_sorted.append((intervals[el][0], el, 0))  # 0 for start of the interval
        intervals_sorted.append((intervals[el][1], el, 1))  # 1 for end of the interval
    intervals_sorted.sort()

    sortlen = intlen * 2
    starts = 0
    ends = 0
    e = 0
    maxx = 0
    starts_count = [0 for _ in range(intlen)]
    ends_count = [0 for _ in range(intlen)]
    diff_count = [0 for _ in range(intlen)]
    while e < sortlen:
        point = intervals_sorted[e][0]
        reference = point
        ce = e
        while point == reference:
            if intervals_sorted[e][2] == 1:
                ends += 1
                e += 1
            else:
                starts += 1
                e += 1
            if e == sortlen:
                break
            point = intervals_sorted[e][0]
        while ce < e:
            if intervals_sorted[ce][2] == 0:  # przy starcie
                starts_count[intervals_sorted[ce][1]] += starts - 1
                ends_count[intervals_sorted[ce][1]] += ends
                ce += 1
            else:
                starts_count[intervals_sorted[ce][1]] += 0
                ends_count[intervals_sorted[ce][1]] += 0
                # diff_count[intervals_sorted[ce][1]] = min(abs(starts - starts_count[intervals_sorted[ce][1]]), abs(ends - ends_count[intervals_sorted[ce][1]]))
                # if min(abs(starts - starts_count[intervals_sorted[ce][1]]), abs(ends - ends_count[intervals_sorted[ce][1]])) > maxx:
                #     maxx = min(abs(starts - starts_count[intervals_sorted[ce][1]]), abs(ends - ends_count[intervals_sorted[ce][1]]))
                ce += 1

    return starts_count, ends_count


# tworzę drugą tablicę w której będę trzymał te przedziały które nie zawierają się w innych przedziałach
# przez całą tablicę L przechodzę i dla każdego sprawdzam czy dany L[i] zawiera się w jakimś przedziale
# w drugiej tablicy jeśli tak to zwiększam poziom danego przedziału a jeśli nie to dokładam L[i]
# na koniec drugiej tablicy, jeśli L[i] zawiera któryś z przedziałów już obecny w tablicy to
# zamieniam to miejsce w tablicy na L[i] i przechodzę jeszcze raz po wszystkich dotychczasowych
# przedziałach aż do i by sprawdzić jego poziom
def better_square(intervals):
    intlen = len(intervals)
    outsiders = [[intervals[0][0], intervals[0][1], 0]]
    maxx = 0

    for i in range(1, intlen):
        belongs_to = False
        for o in range(len(outsiders)):

            if outsiders[o][0] <= intervals[i][0] and intervals[i][1] <= outsiders[o][1]:
                outsiders[o][2] += 1
                if outsiders[o][2] > maxx:
                    maxx = outsiders[o][2]
                belongs_to = True
            if outsiders[o][0] >= intervals[i][0] and intervals[i][1] >= outsiders[o][1]:
                outsiders[o] = [intervals[i][0], intervals[i][1], 0]

                for nw in range(i):
                    if outsiders[o][0] <= intervals[nw][0] and intervals[nw][1] <= outsiders[o][1]:
                        outsiders[o][2] += 1
                        if outsiders[o][2] > maxx:
                            maxx = outsiders[o][2]
                        belongs_to = True

        if not belongs_to:
            outsiders.append([intervals[i][0], intervals[i][1], 0])
    return maxx, outsiders


##################################################


def final(intervals):
    intervals_sorted = []
    intlen = len(intervals)
    for el in range(intlen):
        intervals_sorted.append((intervals[el][0], el, 0))  # 0 for start of the interval
        intervals_sorted.append((intervals[el][1], el, 1))  # 1 for end of the interval
    intervals_sorted.sort()

    print(intervals_sorted)

    # sortlen = intlen * 2
    # old_starts = 0
    # old_ends = 0
    # starts = 0
    # ends = 0
    # e = 0
    # maxx = 0
    # depth_count = [(intlen - 1) for _ in range(intlen)]
    # while e < sortlen:
    #     point = intervals_sorted[e][0]
    #     reference = point
    #     ce = e
    #     while point == reference:
    #         if intervals_sorted[e][2] == 0:
    #             starts += 1
    #             e += 1
    #         if intervals_sorted[e][2] == 1:
    #             e += 1
    #         if e == sortlen:
    #             break
    #         point = intervals_sorted[e][0]
    #     while ce < e:
    #         if intervals_sorted[ce][2] == 0: # przy starcie
    #             depth_count[intervals_sorted[ce][1]] += -old_starts
    #         ce += 1
    #     old_starts = starts
    #
    # e -= 1
    # while e > -1:
    #     point = intervals_sorted[e][0]
    #     reference = point
    #     ce = e
    #     while point == reference:
    #         if intervals_sorted[e][2] == 1:
    #             ends += 1
    #             e -= 1
    #         if intervals_sorted[e][2] == 0:
    #             e -= 1
    #         if e == -1:
    #             break
    #         point = intervals_sorted[e][0]
    #     while ce > e:
    #         if intervals_sorted[ce][2] == 1:
    #             depth_count[intervals_sorted[ce][1]] += -old_ends
    #         ce -= 1
    #     old_ends = ends


    # return max(depth_count)



def depth(L):
    # quantities = [0 for _ in range(len(L))]
    # intervals = (split(L))
    # len_int = len(intervals)
    # quick_sort(intervals, 0, len_int - 1)
    # return quadratic(intervals, quantities)
    return max_interval_count(L)


arr = [[1, 100], [50, 150], [60, 90]]
#x = final(arr)
final(arr)