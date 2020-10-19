from enum import Enum
import time

def lcs(S, n, T, m):

    if n == 0 or m == 0:
        return 0
    if S[n-1] == T[m-1]:
        return 1 + lcs(S, n-1, T, m-1)
    else:
        return max(lcs(S, n-1, T, m), lcs(S, n, T, m-1))

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = make_matrix(m, n, Direction.NA)
    c = make_matrix(m+1, n+1, 0)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = Direction.DIAG
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = Direction.UP
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = Direction.LEFT
    return c, b

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i-1][j-1] == Direction.DIAG:
        print_lcs(b, X, i-1, j-1)
        print(X[i-1])
    elif b[i-1][j-1] == Direction.UP:
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)


def make_matrix(n_rows: int, n_columns: int, val):
    matrix = []
    for i in range(n_rows):
        matrix.append([val] * n_columns)
    return matrix


class Direction(Enum):
    NA = 0
    UP = 1
    LEFT = 2
    DIAG = 3

if __name__ == "__main__":


    x = "AGCGTAG"
    y = "GTCAGA"


    t1 = time.clock()
    a = lcs(x, len(x), y, len(y))
    t2 = time.clock()

    t = t2 - t1
    print("time elapsed: ", t)
    print("LCS: ", a)

    c, b = lcs_length(x, y)


    for i in c:
        print(i)

    print_lcs(b, x, len(x), len(y))

