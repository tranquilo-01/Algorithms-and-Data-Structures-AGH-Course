from zad2testy import runtests
import queue


# djikstra z rozdzieleniem grafu

def robot(L, A, B):
    # 0   N   1           # 3   E   1
    # 1   N   2           # 4   E   2
    # 2   N   3           # 5   E   3

    # 6   W   1           # 9   S   1
    # 7   W   2           # 10  S   2
    # 8   W   3           # 11  S   3

    # 1 -> następny ruch do przodu za cene price[0]
    # 2, 3 analogicznie

    n = len(L)
    m = len(L[0])
    data = [[[None for _ in range(12)] for _ in range(m)] for _ in range(n)]
    pq = queue.PriorityQueue()  # dist, pos, mask
    price = [60, 40, 30]

    pq.put((0, A, 3))

    while not pq.empty():
        dist, pos, mask = pq.get()
        if pos == B:
            return dist

        x, y = pos
        if data[y][x][mask] is None:
            data[y][x][mask] = dist
            if mask in [0, 1, 2]:  # North
                if y - 1 > 0 and L[y - 1][x] == ' ':
                    pq.put((dist + price[mask % 3], (x, y - 1), min(mask + 1, 2)))
                pq.put((dist + 45, pos, 3))
                pq.put((dist + 45, pos, 6))

            elif mask in [3, 4, 5]:  # East
                if x + 1 < m and L[y][x + 1] == ' ':
                    pq.put((dist + price[mask % 3], (x + 1, y), min(mask + 1, 5)))
                pq.put((dist + 45, pos, 0))
                pq.put((dist + 45, pos, 9))

            elif mask in [6, 7, 8]:  # West
                if x - 1 > 0 and L[y][x - 1] == ' ':
                    pq.put((dist + price[mask % 3], (x - 1, y), min(mask + 1, 8)))
                pq.put((dist + 45, pos, 0))
                pq.put((dist + 45, pos, 9))

            elif mask in [9, 10, 11]:  # South
                if y + 1 < n and L[y + 1][x] == ' ':
                    pq.put((dist + price[mask % 3], (x, y + 1), min(mask + 1, 11)))
                pq.put((dist + 45, pos, 3))
                pq.put((dist + 45, pos, 6))

    return None


runtests(robot)