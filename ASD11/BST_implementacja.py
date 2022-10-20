# wstawianie
# min/max
# nastepnik/poprzednik

class Node:
    left = None
    right = None
    parent = None
    val = None

    def __init__(self, val, parent):
        self.parent = parent
        self.val = val

    def insert(self, node):
        if node.val < self.val:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif node.val > self.val:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)


    def min(self):
        if self.left is not None:
            return self.left.min()
        return self

    def next(self):
        if self.right is not None:
            return self.right.min()
        c = self
        p = self.parent
        while p is not None:
            if p.left == c:
                return p
            c = p
            p = p.parent
        return None


def main():
    n10 = Node(10, None)
    n7 = Node(7, n10)
    n4 = Node(4, n7)
    n8 = Node(8, n7)
    n12 = Node(12, n10)
    n17 = Node(17, n12)
    n13 = Node(13, n17)
    n20 = Node(20, n17)
    n10.left = n7
    n10.right = n12
    n7.left = n4
    n7.right = n8
    n12.right = n17
    n17.left = n13
    n17.right = n20
