# znalezc trase przechodzaca przez wszystkie miasta i wracajaca do startowego
# bedzie wykladniczy i tak

# S - podzbior miast
# f(S, t) - dlugosc najkrotszej trasy od miasta 0 do miasta t, przebiegajacej przez wszystkie miasta z S
# Rozwiazanie:
# minimum po wszystkich miastach (t) plus odleglosc z t do 0:
# min (C, t) + d(t, 0)

# rekurencja dla f:
# f(S, t) = min{r e S - t} z ((f(S - t, r) + d(r, t))
# zlozonosc:
# obliczeniowa n^2 * 2^n
# pamieciowa n * 2^n
