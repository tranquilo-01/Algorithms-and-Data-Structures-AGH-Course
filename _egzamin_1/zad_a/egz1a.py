from egz1atesty import runtests


def all_zeros(tab):
    for el in tab:
        if el != 0:
            return False
    return True


def next_day(tab):
    for el in tab:
        if el > 0:
            el -= 1


def snow(S):
    result = 0
    max_ind = -1
    n = len(S)
    while not all_zeros(S):
        for i in range(S):
            if S[i] > max:
                max_ind = i
            if max_ind > n // 2:
                for j in range(n, max_ind):
                    S[j] = 0
            else:
                for j in range(max_ind):
                    S[j] = 0
            result += S[max_ind]
            S[max_ind] = 0
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=False)
