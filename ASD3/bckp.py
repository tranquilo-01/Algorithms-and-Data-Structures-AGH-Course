def partition(tab, l, r):
    i = l - 1
    for j in range(l, r):
        if tab[j] <= tab[r]:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]

    return i + 1


def quick_sort(tab, l, r):
    if l < r:
        q = partition(tab, l, r)
        quick_sort(tab, l, q - 1)
        # l = q + 1
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


def chuujowy(tab):
    tlen = len(tab)
    maxx = 0
    for el1 in range(tlen):
        contains = 0
        start = tab[el1][0]
        end = tab[el1][1]
        for el2 in range(el1 + 1, tlen):
            if tab[el2][0] > end:
                break
            if tab[el2][0] >= start and tab[el2][0] and tab[el2][1] <= end:
                contains += 1
                if contains > maxx:
                    maxx = contains
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
            overlap_count[idx] = - number_of_starts
            number_of_starts += 1
        else:  # end event
            overlap_count[idx] += (number_of_ends - 1)
            if overlap_count[idx] > maxx:
                maxx = overlap_count[idx]
            number_of_ends += 1
    return maxx


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
            if intervals_sorted[ce][2] == 0: # przy starcie
                starts_count[intervals_sorted[ce][1]] += -ends - starts + 1
                ends_count[intervals_sorted[ce][1]] += ends
                ce += 1
            else:
                starts_count[intervals_sorted[ce][1]] += -ends + starts + intlen
                #ends_count[intervals_sorted[ce][1]] += ends
                #diff_count[intervals_sorted[ce][1]] = min(abs(starts - starts_count[intervals_sorted[ce][1]]), abs(ends - ends_count[intervals_sorted[ce][1]]))
                # if min(abs(starts - starts_count[intervals_sorted[ce][1]]), abs(ends - ends_count[intervals_sorted[ce][1]])) > maxx:
                #     maxx = min(abs(starts - starts_count[intervals_sorted[ce][1]]), abs(ends - ends_count[intervals_sorted[ce][1]]))
                # ce += 1

    return starts_count


def final(intervals):
    intervals_sorted = []
    intlen = len(intervals)
    for el in range(intlen):
        intervals_sorted.append((intervals[el][0], el, 0))  # 0 for start of the interval
        intervals_sorted.append((intervals[el][1], el, 1))  # 1 for end of the interval
    intervals_sorted.sort()

    sortlen = intlen * 2
    old_starts = 0
    old_ends = 0
    starts = 0
    ends = 0
    e = 0
    depth_count = [(intlen - 1) for _ in range(intlen)]
    while e < sortlen:
        point = intervals_sorted[e][0]
        reference = point
        ce = e
        while point == reference:
            if intervals_sorted[e][2] == 0:
                starts += 1
                e += 1
            if intervals_sorted[e][2] == 1:
                e += 1
            if e == sortlen:
                break
            point = intervals_sorted[e][0]
        while ce < e:
            if intervals_sorted[ce][2] == 0:
                depth_count[intervals_sorted[ce][1]] += -old_starts
            ce += 1
        old_starts = starts

    e -= 1
    while e > -1:
        point = intervals_sorted[e][0]
        reference = point
        ce = e
        while point == reference:
            if intervals_sorted[e][2] == 1:
                ends += 1
                e -= 1
            if intervals_sorted[e][2] == 0:
                e -= 1
            if e == -1:
                break
            point = intervals_sorted[e][0]
        while ce > e:
            if intervals_sorted[ce][2] == 1:
                depth_count[intervals_sorted[ce][1]] += -old_ends
            ce -= 1
        old_ends = ends


    return max(depth_count)




def better_square(intervals):
    intlen = len(intervals)
    outsiders = [[intervals[0][0], intervals[0][1], 0]]

    for i in range(1, intlen):
        belongs_to = False
        for o in range(len(outsiders)):


            if outsiders[o][0] >= intervals[i][0] and intervals[i][1] >= outsiders[o][1]:
                outsiders[o] = [intervals[i][0], intervals[i][1], 0]

                for nw in range(i):
                    if outsiders[o][0] <= intervals[nw][0] and intervals[nw][1] <= outsiders[o][1]:
                        outsiders[o][2] += 1
                        belongs_to = True
                break

            if outsiders[o][0] <= intervals[i][0] and intervals[i][1] <= outsiders[o][1]:
                outsiders[o][2] += 1
                belongs_to = True



        if not belongs_to:
            outsiders.append([intervals[i][0], intervals[i][1], 0])
            c = len(outsiders) - 1
            for nw in range(i):
                if outsiders[c][0] <= intervals[nw][0] and intervals[nw][1] <= outsiders[c][1]:
                    outsiders[c][2] += 1

    maxx = 0
    for out in outsiders:
        if out[2] > maxx:
            maxx = out[2]

    return maxx