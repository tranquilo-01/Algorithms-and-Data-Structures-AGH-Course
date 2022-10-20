# mamy firme z pracownikami, kazdy pracownik ma wspolczynnik imprezowosci
# impreza jest dozwolona jezeli dla kazdego zaproszonego nie ma na tej imprezie jego bezposrednich podwladnch
# szukamy wartosci najlepszej imprezy - sumy wspolczynnikow wszystkich zaproszonych


class Employee:
    def __init__(self, fun):
        self.fun = fun  # wspolczynnik imprezowosci
        self.emp = []  # tablica pracownikow nizszego szczebla
        self.f = -1  # wartosc funkcji f od pracownika
        self.g = -1  # wartosc funkcji g od pracownika


def f(v):  # wartosc najlepszej imprezy poddrzewa zakorenionego w v
    if v.f != -1:
        return v.f
    f1 = g(v)
    f2 = v.fun
    for u in v.emp:
        f2 += g(u)
    v.f = max(f1, f2)
    return v.f


def g(v):  # to co f tylko v nie idzie na impreze
    if v.g != -1:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g


# wynikiem bedzie f(root)
