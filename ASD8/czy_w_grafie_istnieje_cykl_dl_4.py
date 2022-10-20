# Dany jest graf nieskierowany G zawierajacy n wierzchołków. Zaproponuj
# algorytm, który stwierdza czy w G istnieje cykl składajacy sie z dokładnie 4 wierzchołków. Zakładamy, ze
# graf reprezentowany jest przez macierz sasiedztwa A ( nie ma O(v^2))

# 1. najprostsze O(v^4) sprawdzic kazde 4 wierzcholki

# 2. ten lepszy w O(v^3)
def brute(G):
    n = len(G)
    counter = 0
    for a in range(n):
        for b in range(a+1, n):
            for i in range(0, n):
                if i != a and i != b and G[a][i] and G[i][b]:
                    counter += 1
            if counter >= 2:
                return True
    return False

