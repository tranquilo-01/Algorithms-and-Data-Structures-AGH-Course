# radix sort - sortowanie pozycyjnie. sortuje dane po pozycjiach od najmniej do najbardziej istotnych
# nie jest samodzielne - najczesciej uzywa counting sorta

# przyklad - sortowanie liczb n-cyfrowych

def radix_sort(tab, n):
    for i in range(0, n):
        counting_sort(tab, i)


def get_digit(number, n):
    return number // 10**n % 10


def counting_sort(tab, ind):
    n = len(tab)
    counts = [0] * 10
    srtd = [0] * n

    # counting
    for x in tab:
        counts[get_digit(x, ind)] += 1

    # cumulating
    for i in range(1, 10):
        counts[i] += counts[i - 1]

    # sorting
    for i in range(n - 1, -1, -1):
        srtd[counts[get_digit(tab[i], ind)] - 1] = tab[i]
        counts[get_digit(tab[i], ind)] -= 1

    # copying from srtd to input tab
    for i in range(n):
        tab[i] = srtd[i]


arr = [2137, 4200, 6969, 6900, 7129, 3257, 1732, 5846, 2468, 3611, 3446, 2573]
radix_sort(arr, 4)
print(arr)
