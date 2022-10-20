from random import randint


def natural2d(n, low, hi):
    arr = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            arr[i][j] = randint(low, hi)
    return arr


def natural3d(n, low, hi):
    arr = [[[0 for x in range(n)] for y in range(n)] for z in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr[i][j][k] = randint(low, hi)
    return arr


def naturalarray(length, low, high):
    """uzupelnia tablice o podanej dlugosci liczbami naturalnymi w zakresie low - high"""
    array = []
    for i in range(length):
        array.append(randint(low, high))
    return array


def is_prime(a):
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1
    return True


def printbyrows(arr):
    for i in range(len(arr)):
        print(arr[i])


def sasiadujace(tab, row, column):
    tlen = len(tab)
    ret = [0] * 9
    i = 0

    for x in range(row - 1, row + 2):
        for y in range(column - 1, column + 2):
            if y < 0 or x < 0 or y > tlen - 1 or x > tlen - 1 or (x == row and y == column):
                ret[i] = -1
                i += 1
            else:
                ret[i] = tab[x][y]
                i += 1
    return ret


def bin_to_dec(b):
    b = int(b)
    dec = 0
    i = 0
    while b > 0:
        dec += (b % 10) * (2 ** i)
        b //= 10
        i += 1
    return dec


def get_bitmask(decimalstr, lgh):
    dec = int(decimalstr)
    binary = ""
    while dec >= 1:
        if dec % 2 == 1:
            binary = "1" + binary
            dec = dec // 2
        else:
            binary = "0" + binary
            dec = dec // 2
    while len(binary) < lgh:
        binary = "0" + binary
    return binary


def dec_to_bin(dec):
    binary = ""
    while dec >= 1:
        if dec % 2 == 1:
            binary = "1" + binary
            dec = dec // 2
        else:
            binary = "0" + binary
            dec = dec // 2
    return binary


def tab2list(t):
    n = len(t)
    p = None

    for i in range(n - 1, -1, -1):
        q = Node()
        q.val = t[i]
        q.next = p
        p = q

    return p


def list2tab(l):
    t = []
    while l is not None:
        t.append(l.val)
        l = l.next

    return t


def print_list(first):
    while first is not None:
        print(first.val, end=" ")
        first = first.next
    print()


class Node:
    def __init__(self):
        self.val = None
        self.next = None
