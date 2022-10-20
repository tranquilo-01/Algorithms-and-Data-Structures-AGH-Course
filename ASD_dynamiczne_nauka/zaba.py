from math import inf


def zaba_rek(road, i, energy):
    if i >= len(road) or i + energy >= len(road):
        return 0

    minn = inf
    for k in range(1, energy):
        res = zaba_rek(road, i + k, energy - k + road[i + k]) + 1
        minn = min(res, minn)
    return minn


def zaba_memo(road):
    lookup = [[-1 for _ in range(sum(road) + 1)] for _ in range(len(road))]

    def rek(i, energy):
        if i >= len(road) or i + energy >= len(road):
            return 0

        if lookup[i][energy] != -1:
            return lookup[i][energy]

        minn = inf
        for k in range(1, energy):
            res = rek(i + k, energy - k + road[i + k]) + 1
            minn = min(res, minn)
        lookup[i][energy] = minn
        return lookup[i][energy]

    r = rek(0, road[0])
    return r


droga = [3, 1, 1, 6, 1, 1, 1, 1, 1, 3, 0, 0, 1, 1, 1, 1, 4, 2, 1, 1, 1, 4, 5, 6, 10, 0, 0, 0, 0, 0, 0]
print(zaba_rek(droga, 0, droga[0]))
print(zaba_memo(droga))
