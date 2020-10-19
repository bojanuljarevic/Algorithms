import random

class Data:

    def __init__(self, key, literal):
        self.key = key
        self.literal = literal

    def printData(self):
        print(self.key, self.literal)


def h1(k, m):
    return k % m

def h2(k, m):
    return 1 + (k % (m-1))

def linearProbing(k, m, i):
    return (h1(k,m) + i) % m

def quadraticProbing(k, m, i):
    return (h1(k,m) + 0.5*i + 0.5*i*i) % m

def doubleHashing(k, m):
    return (h1(k,m) + h2(k,m)) % m

def hashInsert(T, x, m):
    i = 0
    try:
        while i < m:
            j = linearProbing(x.key, m, i)
            if T[j] == None:
                T[j] = x
                return j
            else:
                i += 1
    except:
        print("hash table overflow")
        return None

def hashSearch(T, x, m):
    i = 0
    j = linearProbing(x.key, m, i)
    while (T[j] == None or i == m) == False:
        j = linearProbing(x.key, m, i)
        if T[j] == x:
            return j
        i += 1
    return None


if __name__ == "__main__":

    n = 10
    T = [None for i in range(n)]
    for i in range(48, 48+n):
        el = random.randint(48, 48 + n)
        d = Data(el, chr(el))
        hashInsert(T, d, n)

    for i in T:
        i.printData()

