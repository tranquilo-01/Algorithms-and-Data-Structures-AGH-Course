# sortowanie listy

class Node():
    def __init__(self, key):
        self.data = key
        self.next = None


def sort(first):
    res = None
    guard = Node(-1)
    guard.next = first
    first = guard
    while first.next is not None:
        maxi = find_max_and_remove(first)
        maxi.next = res
        res = maxi
    return res


def find_max_and_remove(first):
    if first.next is None:
        return first
    maxel = first.data
    maxprev = first
    tmp = first.next
    prevtmp = first
    while tmp is not None:
        if maxel.data < tmp.data:
            maxprev = prevtmp
            maxel = tmp
        prevtmp = tmp
        tmp = tmp.next
        maxprev.next = maxel.next
    return maxel
