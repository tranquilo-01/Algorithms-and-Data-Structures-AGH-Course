# def f(cost):
#     n = len(cost)
#     lu = [[0 for _ in range(n)] for _ in range(n)]
#
#     lu[cost[0]][0] = 1
#     for i in range(1, n):
#         for e in range(n):
#             if lu[e][i]:
#                 if i < n - 1:
#                     if e + cost[i] - 1 >= n:
#                         lu[n - 1][i + 1] = lu[e][i] + 1
#                     elif e + cost[i] - 1 >= 0:
#                         lu[e + cost[i] - 1][i + 1] = lu[e][i] + 1
#             if e < n - 1 and lu[e + 1][i - 1]:
#                 lu[e][i] = lu[e + 1][i - 1]
#                 if i < n - 1:
#                     if e + cost[i] - 1 >= n:
#                         lu[n - 1][i + 1] = lu[e][i] + 1
#                     elif e + cost[i] - 1 >= 0:
#                         lu[e + cost[i] - 1][i + 1] = lu[e][i] + 1
#
#     return restore_jumps(lu)
#
#
# def restore_jumps(lu):
#     n = len(lu)
#     minn = 10 ** 6
#     curr_e = 0
#     to_ret = []
#     for x in range(n):
#         if 0 < lu[x][n - 1] < minn:
#             minn = lu[x][n - 1]
#             curr_e = x
#
#     curr_i = n - 1
#     while curr_i >= 0 and curr_e < n:
#         number = lu[curr_e][curr_i]
#         while curr_e < n and curr_i >= 0 and lu[curr_e][curr_i] == number:
#             curr_i -= 1
#             curr_e += 1
#         to_ret = [curr_i] + to_ret
#         number -= 1
#         while curr_e < n and curr_i >= 0 and lu[curr_e][curr_i] != number:
#             curr_e -= 1
#
#     if to_ret[0] == -1:
#         to_ret[0] = 0
#     elif to_ret[0] != 0:
#         to_ret = [0] + to_ret
#
#     return to_ret
import heapq

def f(tab):
    n = len(tab)
    lu = [[0 for _ in range(n)] for _ in range(n)]

    lu[tab[0]][0] = 1
    for i in range(1, n):
        for e in range(n):
            if lu[e][i]:
                if i < n - 1:
                    if e + tab[i] - 1 >= n:
                        lu[n - 1][i + 1] = lu[e][i] + 1
                    elif e + tab[i] - 1 >= 0:
                        lu[e + tab[i] - 1][i + 1] = lu[e][i] + 1
            if e < n - 1 and lu[e + 1][i - 1]:
                lu[e][i] = lu[e + 1][i - 1]
                if i < n - 1:
                    if e + tab[i] - 1 >= n:
                        lu[n - 1][i + 1] = lu[e][i] + 1
                    elif e + tab[i] - 1 >= 0:
                        lu[e + tab[i] - 1][i + 1] = lu[e][i] + 1

    return restore_jumps(lu)


def greedy(tab):
    n = len(tab)
    heap = []
    results = [0]
    curr_max = tab[0]
    for i in range(1, tab[0] + 1):
        heap.append((-tab[i], -i))

    heapq.heapify(heap)

    while curr_max < n:
        el = heapq.heappop(heap)
        results.append(-el[1])
        next_max = curr_max + curr_max + el[1] - el[0]
        if next_max < n:
            for i in range(curr_max+1, next_max):
                heapq.heappush(heap, (-tab[i], -i))
        curr_max = next_max

    results.sort()
    return results


arr = [7, 0, 0, 1, 0, 3, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0]
print(greedy(arr))
