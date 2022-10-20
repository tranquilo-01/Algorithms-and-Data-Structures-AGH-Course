# Mateusz Zając, 407807

# Algorytm bazuje na funkcji rekurencyjnej:

# f(b, i) = max(
#               f(b, i - 1)
#               f(b - w[i], p[i]) + s[i]
# ); b >= 0 and i >= 0
# f(b, i) = 0; b < 0 or i < 0

# gdzie b oznacza obecny budżet, i oznacza obecny akademik,
# w[i] oznacza cenę obecnego akademika
# p[i] oznacza najbliższy akademik od lewej, który nie pokrywa się z obecnym
# s[i] oznacza ilość studentów, która mieści się w obecnym akademiku

# Potrzebuję posortować listę akademików rosnąco po prawych współrzędnych
# Następnie tworzę tablicę, w której wierszami są wszystkie możliwe wartości budżetu od 0 do p,
# a kolumnami konkretne, już posortowane akademiki

# złożoność obliczeniowa algorytmu to O(np + nlogn), gdzie p oznacza budżet, a n ilość akademików
# pamięciowa to O(np) z powodu prostokątnej listy, ale używam dodatkowej listy o rozmiarze n


from zad4testy import runtests


def get_left_neighbours(dorms):
    """ Dla każdego akademika, znajdź jego najbliższego, lewego sąsiada,
    z którym się nie pokrywa."""

    left_neighbour = [-1 for _ in dorms]

    for i in range(len(dorms)):
        for j in range(len(dorms) - 1, -1, -1):
            if dorms[j][2] < dorms[i][1]:
                left_neighbour[i] = j
                break

    return left_neighbour


def create_dynamic_util(list_, max_budget):
    """ Stwórz listę dwuwymiarową służącą do spamiętywania poprzednich obliczeń.
    wiersze - wszystkie możliwe wartości budżetu
    kolumny - wszystkie akademiki (po posortowaniu)
    Każda komórka zawiera ilość studentów i krotkę akademików najlepszej możliwej kombinacji
    dla danego budżetu i ostatniego wybieranego akademika
    """

    dynamic_util = []
    for _ in range(max_budget + 1):
        row = [(0, tuple()) for _ in list_]
        dynamic_util.append(row)

    return dynamic_util


def get_students(building):
    """ Ilość studentów w akademiku równa się polu prostokąta o bokach
    (b - a) i h, gdzie a i b to lewa i prawa współrzędna akademika,
    a h to jego wysokość """

    h, a, b, _, _ = building
    return (b - a) * h


def select_buildings(T, p):
    """ Rdzeń algorytmu dynamicznego, opisany na początku pliku """

    # chcę zachować indeksy po posortowaniu,
    # bo jak widzę, sprawdzarka oczekuje indeksów akademików
    # z pierwotnej listy
    dorms = [T[i] + (i,) for i in range(len(T))]

    dorms.sort(key=lambda x: x[2])
    left_neighbours = get_left_neighbours(dorms)
    results = create_dynamic_util(dorms, p)

    for budget in range(1, p + 1):
        for dorm in range(len(dorms)):
            neighbour = left_neighbours[dorm]

            if dorm != 0:
                next_result = results[budget][dorm - 1]
                if next_result[0] > results[budget][dorm][0]:  # nie branie aktualnego
                    results[budget][dorm] = next_result

            if budget - dorms[dorm][3] >= 0:  # branie aktualnego jesli wiekszy od nie brania
                next_result = (0, tuple())
                if neighbour >= 0:
                    next_result = results[budget - dorms[dorm][3]][neighbour]
                next_result = (
                    next_result[0] + get_students(dorms[dorm]),
                    next_result[1] + (dorms[dorm][4],)  # indeks akademika w T
                )
                if next_result[0] > results[budget][dorm][0]:
                    results[budget][dorm] = next_result

    # for row in results:
    #     print(row)
    return results[-1][-1][1]


runtests(select_buildings)
