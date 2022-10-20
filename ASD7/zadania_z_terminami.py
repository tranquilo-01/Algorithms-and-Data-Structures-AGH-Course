def choose(Z, start):  # kazdy z ma deadline i profit
    Z.sort(key=lambda x: x.p)
    Z.sort(key=lambda x: x.d, reverse=True)

    ret = []
    while Z and Z[0].deadline >= start:
        f = Z[0]
        ret.append(f)
        Z.pop[0]
        for e in z:
            if e.d != f.d:
                break
            e.d-=1
        Z.sort(key=lambda x: x.p)
        Z.sort(key=lambda x: x.d, reverse=True)
    return ret


