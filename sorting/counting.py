
import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def counting_sort(A, B, k):
    C = [0] * k
    for j in A:
        C[j] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1


A = random_list(0, 100, 100)
B = [0] * len(A)
k = max(A) + 1
print("COUNTING SORT(100):")
print("Inicijalni niz: ", A)
t1 = time.clock()
counting_sort(A, B, k)
t2 = time.clock()
print("Sortirani niz: ", B)
print("Trajanje: ", t2 - t1)

A = random_list(0, 1000, 1000)
B = [0] * len(A)
k = max(A) + 1
print("COUNTING SORT(1K):")
t1 = time.clock()
counting_sort(A, B, k)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

A = random_list(0, 10000, 10000)
B = [0] * len(A)
k = max(A) + 1
print("COUNTING SORT(10K):")
t1 = time.clock()
counting_sort(A, B, k)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

A = random_list(0, 100000, 100000)
B = [0] * len(A)
k = max(A) + 1
print("COUNTING SORT(100K):")
t1 = time.clock()
counting_sort(A, B, k)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

A = random_list(0, 1000000, 1000000)
B = [0] * len(A)
k = max(A) + 1
print("COUNTING SORT(1M):")
t1 = time.clock()
counting_sort(A, B, k)
t2 = time.clock()
print("Trajanje: ", t2 - t1)