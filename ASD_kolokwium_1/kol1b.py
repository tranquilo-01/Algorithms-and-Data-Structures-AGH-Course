# Krzysztof Dziechciarz
# kazde slowo w tablicy sortujemy wewnetrznie wg charow. np slowo wilk zostanie posortowane na iklw (counting)
# posortowane slowa wpisujemy do nowej tablicy i sortujemy (bucket + radix)
# nastepnie przechodzimy po nowej tablicy i sprawdzamy ktory ciag znakow wystepuje najwiecej razy
# wszytskie opracje maja zlozonosc liniowa, wiec algorytm ma zlozonosc O(n), gdzie n to suma dlugosci
# napisow w tablicy wejsciowej

from kol1btesty import runtests


# funkcja przekształca napis na posortowany ciag charow
def make_char(napis):
    clen = len(napis)

    # teraz posortujemy tablice counting_sortem
    counts = [0] * 26
    final = [0] * clen

    for c in napis:
        counts[ord(c) - 97] += 1

    for i in range(1, 26):
        counts[i] = counts[i] + counts[i - 1]

    for i in range(clen - 1, -1, -1):
        final[counts[ord(napis[i]) - 97] - 1] = napis[i]
        counts[ord(napis[i]) - 97] -= 1

    to_ret = ""
    for c in final:
        to_ret += c

    return to_ret


# funkcja tworzy nową tablicę z posortowanymi ciagami liter
def make_new_array(tab):
    new_array = []
    for s in tab:
        new_array.append(make_char(s))
    return new_array


def radix_sort(tab, slen):
    for i in range(1, slen + 1):
        counts = [0] * 26
        final = [""] * len(tab)

        for s in tab:
            counts[ord(s[-i]) - 97] += 1

        for j in range(1, len(counts)):
            counts[j] += counts[j - 1]

        for k in range(len(tab) - 1, -1, -1):
            final[counts[ord(tab[k][-i]) - 97] - 1] = tab[k]
            counts[ord(tab[k][-i]) - 97] -= 1

        for l in range(len(tab)):
            tab[l] = final[l]


# funkcja sortuje tablice napisow po dlugosci, a nastepnie alfabetycznie
def sort_new_array(tab):
    max_word_len = 0
    for word in tab:
        wlen = len(word)
        if wlen > max_word_len:
            max_word_len = wlen

    # najpierw tworze kubelki gdzie bede umieszczal slowa o takiej samej dlugosci
    buckets = [[] for _ in range(max_word_len)]
    for word in tab:
        wlen = len(word)
        buckets[wlen - 1].append(word)

    for word_len in range(0, max_word_len):
        words = buckets[word_len]

        if len(words) > 1:
            # radix sort
            radix_sort(words, word_len)

    to_ret = []
    for bucket in buckets:
        for word in bucket:
            to_ret.append(word)

    return to_ret


def f(tab):
    na = make_new_array(tab)
    alen = len(na)
    na = sort_new_array(na)

    max_pop = 0
    i = 0
    j = 0
    while j < alen:
        cur_max = 0
        while j < alen and na[i] == na[j]:
            cur_max += 1
            j += 1
        if cur_max > max_pop:
            max_pop = cur_max
        i = j

    return max_pop


arr = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
f(arr)

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(f, all_tests=True)
