def przedzialy(t):
    a = 1
    t.sort()
    curr = t[0]

    for el in t[1:]:  # dla kazdej liczby rozwazamy czy jest w aktualnym przedziale jak nie to robimy nowy
        if el > curr + 1:
            a += 1
            curr = el
    return a
