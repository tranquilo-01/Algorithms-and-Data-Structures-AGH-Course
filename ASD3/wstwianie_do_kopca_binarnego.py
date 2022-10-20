# wstawianie do drzewa kompletnego
# kopiec numerujemy od 1, a w zerowym indeksie przechwujemy dlugosc kopca
import math
from io import StringIO


def parent(n):
    return n // 2


def left(n):
    return 2 * n


def right(n):
    return 2 * n + 1


def add(tab, val):
    # dodajemy element na koniec
    tab[0] += 1
    tab[tab[0]] = val

    # dopóki się da zamieniamy ze swoim rodzicem (zeby byla dobra kolejnosc)

    i = tab[0]
    while tab[parent(i)] < tab[i] and parent(i) > 0:
        tab[parent(i)], tab[i] = tab[i], tab[parent(i)]
        i = parent(i)


def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return


tree = [0 for i in range(100)]
add(tree, 2)
print(tree)
add(tree, 1)
print(tree)
add(tree, 3)
print(tree)
add(tree, 7)
print(tree)
add(tree, 4)
print(tree)
add(tree, 2)
print(tree)
add(tree, 0)
print(tree)
add(tree, 6)
print(tree)
add(tree, 9)
print(tree)
add(tree, 69)
print(tree)
add(tree, 420)
print(tree)
add(tree, 2137)
show_tree(tree, 100)


