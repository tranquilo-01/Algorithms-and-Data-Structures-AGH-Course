from zad5testy import runtests
import heapq


def restore_jumps(lu):
    n = len(lu)
    minn = 10 ** 6
    curr_e = 0
    to_ret = []
    for x in range(n):
        if 0 < lu[x][n - 1] < minn:
            minn = lu[x][n - 1]
            curr_e = x

    curr_i = n - 1
    while curr_i >= 0 and curr_e < n:
        number = lu[curr_e][curr_i]
        while curr_e < n and curr_i >= 0 and lu[curr_e][curr_i] == number:
            curr_i -= 1
            curr_e += 1
        to_ret = [curr_i] + to_ret
        number -= 1
        while curr_e < n and curr_i >= 0 and lu[curr_e][curr_i] != number:
            curr_e -= 1

    if to_ret[0] == -1:
        to_ret[0] = 0
    elif to_ret[0] != 0:
        to_ret = [0] + to_ret

    return to_ret


def greedy(tab):
    n = len(tab)
    heap = []
    results = [0]
    curr_max = tab[0]
    for i in range(1, tab[0] + 1):
        heap.append((-tab[i], -i))

    heapq.heapify(heap)
    prev = (0, 0)
    while curr_max < n-1:
        el = heapq.heappop(heap)
        results.append(-el[1])
        next_max = curr_max - el[0]
        if next_max < n-1:
            for i in range(curr_max+1, next_max+1):
                heapq.heappush(heap, (-tab[i], -i))
        curr_max = next_max
        prev = el

    results.sort()
    return results







def plan(T):
    return greedy(T)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
