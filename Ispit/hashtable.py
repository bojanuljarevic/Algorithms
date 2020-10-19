import math
from enum import Enum
from math import floor
import random


class Data:

    def __init__(self, key = None, literal = None):
        self.key = key
        self.literal = literal

class HashType(Enum):
    DIVISION = 0
    MULTIPLICATION = 1
    UNIVERSAL = 2
    LINEAR = 3
    QUADRATIC = 4
    DOUBLE = 5

class HashTable:

    def __init__(self, m = 20):
        self.table = []
        self.m = m
        for i in range(m):
            self.table.append([])

    def hash(self, k, hashType = HashType.DIVISION):
        if hashType == HashType.DIVISION:
            return k % self.m
        elif hashType == HashType.MULTIPLICATION:
            A = (math.sqrt(5) - 1) / 2
            return floor(self.m * (k * A % 1))
        else:
            p = random.randint(k + 1, 2 * k)
            while not isPrime(p):
                p = random.randint(k + 1, 2 * k)
                a = random.randint(1, p-1)
                b = random.randint(0, p-1)
                return ((a*k + b) % p) % self.m

    def chainedHashInsert(self, x):
        self.table[x.key].insert(0, x.literal)

    def chainedHashSearch(self, k):
        for i in self.table[self.hash(k)]:
            if i == k:
                return i

    def chainedHashDelete(self, x):
        for i in self.table[self.hash(x)]:
            if i == x:
                self.table[self.hash(x)].remove(x)


    def openAddressing(self, k, hashType = HashType.LINEAR):
        if hashType == HashType.LINEAR:
            for i in range(self.m):
                if self.table[((k % self.m + i) % self.m)] == []:
                    return (k % self.m + i) % self.m
            return None
        elif hashType == HashType.QUADRATIC:
            for i in range(self.m):
                if self.table[floor((k % self.m + 0.5*i + 0.5*i*i) % self.m)] == []:
                    return floor((k % self.m + 0.5*i + 0.5*i*i) % self.m)
            return None
        else:
            for i in range(self.m):
                if self.table[floor((k % self.m + 1 + (k % (self.m-1))) % self.m)] == []:
                    return floor((k % self.m + 1 + (k % (self.m-1))) % self.m)
            return None

    def hashInsert(self, k):
        for i in range(self.m):
            j = self.openAddressing(k, HashType.QUADRATIC)
            if self.table[j] == []:
                self.table[j] = k
                return j
        print("hash table overflow")

    def hashSearch(self,  k):
        i = 0
        j = self.openAddressing(k)
        while self.table[j] != None and i != self.m:
            j = self.openAddressing(k)
            if self.table[j] == k:
                return j
            i += 1
        return None


def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1


if __name__ == "__main__":

    ht = HashTable(15)

    for i in range(10):
        x = random.randint(0, 100)
        ht.hashInsert(x)


    for i in ht.table:
        print(i)

    '''
    print(ht.chainedHashSearch(2))

    ht.chainedHashDelete(2)

    print(ht.chainedHashSearch(2))
    '''