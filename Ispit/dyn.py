import numpy as np
from enum import Enum

class Arrow(Enum):
    UP = 0
    LEFT = 127
    DIAG = 255

def LCS_Length(X, Y):
    m = len(X)
    n = len(Y)
    b = np.array([None]*(m*n)).reshape(m, n)
    c = np.array([None] * ((m+1)*(n+1))).reshape(m+1, n+1)
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = Arrow.DIAG
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = Arrow.UP
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = Arrow.LEFT
    return c, b

def print_LCS(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == Arrow.DIAG:
        print_LCS(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == Arrow.UP:
        print_LCS(b, X, i-1, j)
    else:
        print_LCS(b, X, i, j-1)

if __name__ == "__main__":

    X = "ABCBDAB"
    Y = "BDCABA"
    c, b = LCS_Length(X, Y)
    print(c)
    print_LCS(b, X, len(X)-1, len(Y)-1)
