
import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def bucket_sort(A):
    n = len(A)
    size = max(A) + 1
    B = []
    for i in range(0, size):
        B.append([])
    for i in range(0, n):
        j = (n * A[i]) // size + 1
        B[j].append(A[i])
    for i in range(0, n):
        insertion_sort(B[i])
    A[:] = [y for x in B for y in x]



l = random_list(0, 101, 100)
print("BUCKET SORT(100):")
t1 = time.clock()
print("Inicijalni niz: ", l)
bucket_sort(l)
print("Sortirani niz: ", l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 1001, 1000)
print("BUCKET SORT(1K):")
t1 = time.clock()
bucket_sort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 10001, 10000)
print("BUCKET SORT(10K):")
t1 = time.clock()
bucket_sort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 100001, 100000)
print("BUCKET SORT(100K):")
t1 = time.clock()
bucket_sort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 1000001, 1000000)
print("BUCKET SORT(1M):")
t1 = time.clock()
bucket_sort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)
