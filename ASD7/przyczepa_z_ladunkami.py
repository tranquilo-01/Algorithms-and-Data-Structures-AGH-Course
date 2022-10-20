def ladunek(P, K):
    K.sort(reverse=True)
    ile = 0
    ret = []
    for i in K:
        if P >= i:
            ret.append(i)
            P -= i
    return ret
