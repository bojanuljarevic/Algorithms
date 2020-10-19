import math
import random
import time

class Data:

    def __init__(self, key, literal):
        self.key = key
        self.literal = literal

    def printData(self):
        print(self.key, self.literal)


def divisionHash(table, key):
    return key % len(table)

def multiplicationHash(table, key):
    return math.floor(len(table * ((key * 0.6180339887) % 1)))

def universalHash(table, key, p):
    a = random.randint(1, p)
    b = random.randint(0, p)
    return ((a*key + b) % p) % len(table)


def chainedHashInsert(table, x, p):
    index = universalHash(table, x.key, p)
    table[index].insert(0, x)

def chainedHashSearch(table, key):
    for i in table:
        if i:
            if i[0].key == key:
                return i[0].literal
    return None

def chainedHashDelete(table, x):
    for i in table:
        if i:
            if i[0].key == x.key:
                table.remove(i)


if __name__ == "__main__":

    p1 = 23
    p2 = 9973
    p3 = 99991

    m1p1 = p1
    m2p1 = p1 // 2
    m3p1 = p1 // 4

    m1p2 = p2
    m2p2 = p2 // 2
    m3p2 = p2 // 4

    m1p3 = p3
    m2p3 = p3 // 2
    m3p3 = p3 // 4

    n1 = 10000
    n2 = 50000
    n3 = 100000

    '''
    # p = 23, m = p, n = 10 000

    HashTable = [[] for i in range(m1p1)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p1-1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m1p1, n1): ",t2 - t1)


    # p = 23, m = p / 2, n = 10 000

    HashTable = [[] for i in range(m2p1)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p1-1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m2p1, n1): ",t2 - t1)

    # p = 23, m = p / 4, n = 10 000

    HashTable = [[] for i in range(m3p1)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p1-1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m3p1, n1): ",t2 - t1)

    # p = 23, m = p, n = 50 000

    HashTable = [[] for i in range(m1p1)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p1 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m1p1, n2): ", t2 - t1)

    # p = 23, m = p / 2, n = 50 000

    HashTable = [[] for i in range(m2p1)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p1 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m2p1, n2): ", t2 - t1)

    # p = 23, m = p / 4, n = 50 000

    HashTable = [[] for i in range(m3p1)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p1 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m3p1, n2): ", t2 - t1)
    

    # p = 23, m = p, n = 100 000

    HashTable = [[] for i in range(m1p1)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p1 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m1p1, n3): ", t2 - t1)

    # p = 23, m = p / 2, n = 100 000

    HashTable = [[] for i in range(m2p1)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p1 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m2p1, n3): ", t2 - t1)

    # p = 23, m = p / 4, n = 100 000

    HashTable = [[] for i in range(m3p1)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p1 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p1, m3p1, n3): ", t2 - t1)



    # p = 9973, m = p, n = 10 000

    HashTable = [[] for i in range(m1p2)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m1p2, n1): ", t2 - t1)

    # p = 9973, m = p / 2, n = 10 000

    HashTable = [[] for i in range(m2p2)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m2p2, n1): ", t2 - t1)

    # p = 9973, m = p / 4, n = 10 000

    HashTable = [[] for i in range(m3p2)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m3p2, n1): ", t2 - t1)

    # p = 9973, m = p, n = 50 000

    HashTable = [[] for i in range(m1p2)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m1p2, n2): ", t2 - t1)

    # p = 9973, m = p / 2, n = 50 000

    HashTable = [[] for i in range(m2p2)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m2p2, n2): ", t2 - t1)

    # p = 9973, m = p / 4, n = 50 000

    HashTable = [[] for i in range(m3p2)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m3p2, n2): ", t2 - t1)

    # p = 9973, m = p, n = 100 000

    HashTable = [[] for i in range(m1p2)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m1p2, n3): ", t2 - t1)

    # p = 23, m = p / 2, n = 100 000

    HashTable = [[] for i in range(m2p2)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m2p2, n3): ", t2 - t1)

    # p = 9973, m = p / 4, n = 100 000

    HashTable = [[] for i in range(m3p2)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p2 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p2)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p2, m3p2, n3): ", t2 - t1)
    
    '''

    # p = 99991, m = p, n = 10 000

    HashTable = [[] for i in range(m1p3)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m1p3, n1): ", t2 - t1)

    # p = 99991, m = p / 2, n = 10 000

    HashTable = [[] for i in range(m2p3)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m2p3, n1): ", t2 - t1)

    # p = 99991, m = p / 4, n = 10 000

    HashTable = [[] for i in range(m3p3)]
    t1 = time.clock()
    for i in range(0, n1):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m3p3, n1): ", t2 - t1)

    # p = 99991, m = p, n = 50 000

    HashTable = [[] for i in range(m1p3)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m1p3, n2): ", t2 - t1)

    # p = 99991, m = p / 2, n = 50 000

    HashTable = [[] for i in range(m2p3)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m2p3, n2): ", t2 - t1)

    # p = 99991, m = p / 4, n = 50 000

    HashTable = [[] for i in range(m3p3)]
    t1 = time.clock()
    for i in range(0, n2):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m3p3, n2): ", t2 - t1)

    # p = 99991, m = p, n = 100 000

    HashTable = [[] for i in range(m1p3)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m1p3, n3): ", t2 - t1)

    # p = 99991, m = p / 2, n = 100 000

    HashTable = [[] for i in range(m2p3)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m2p3, n3): ", t2 - t1)

    # p = 99991, m = p / 4, n = 100 000

    HashTable = [[] for i in range(m3p3)]
    t1 = time.clock()
    for i in range(0, n3):
        el = random.randint(0, p3 - 1)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p3)
    t2 = time.clock()
    print("Vrijeme izvršavanja(p3, m3p3, n3): ", t2 - t1)
    


    # Testiranje funkcija Search i Delete

    HashTable = [[] for i in range(5)]
    for i in range(0, 20):
        el = random.randint(74, 79)
        d = Data(el, chr(el))
        chainedHashInsert(HashTable, d, p1)

    print(chainedHashSearch(HashTable, 77))

    chainedHashDelete(HashTable, Data(77, chr(77)))

    print(chainedHashSearch(HashTable, 77))
