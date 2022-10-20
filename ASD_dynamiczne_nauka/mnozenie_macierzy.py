# Dany jest cieg macierzy A1,A2, . . . ,An. Ktos chce policzyc iloczyn
# A1A2...An. Macierze nie sa koniecznie kwadratowe (ale oczywiscie znamy ich rozmiary). Zaleznie w jakiej
# kolejnosci wykonujemy mnozenia, koszt obliczeniowy moze byc rózny—nalezy podac algorytm znajdujacy
# koszt mnozenia przy optymalnym doborze kolejnosci.

# A naive recursive implementation that
# simply follows the above optimal
# substructure property
import sys


# Matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n


def matrix_chain_order_exponential(p, i, j):
    if i == j:
        return 0

    _min = sys.maxsize

    # place parenthesis at different places
    # between first and last matrix,
    # recursively calculate count of
    # multiplications for each parenthesis
    # placement and return the minimum count
    for k in range(i, j):

        count = (matrix_chain_order_exponential(p, i, k)
                 + matrix_chain_order_exponential(p, k + 1, j)
                 + p[i - 1] * p[k] * p[j])

        if count < _min:
            _min = count

    # Return minimum count
    return _min


dp = [[-1 for i in range(100)] for j in range(100)]


# Function for matrix chain multiplication
def matrixChainMemoised(p, i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize

    for k in range(i, j):
        dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j) + p[i - 1] * p[k] * p[j])

    return dp[i][j]


def MatrixChainOrder(p, n):
    i = 1
    j = n - 1
    return matrixChainMemoised(p, i, j)
