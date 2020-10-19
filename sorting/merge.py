#!/usr/bin/python

import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]

    i = j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


l = random_list(0, 100, 100)
t1 = time.clock()
merge_sort(l, 0, len(l)-1)
t2 = time.clock()
print("MERGE(100): ", t2 - t1)

l = random_list(0, 1000, 1000)
t1 = time.clock()
merge_sort(l, 0, len(l)-1)
t2 = time.clock()
print("MERGE(1K): ", t2 - t1)

l = random_list(0, 10000, 10000)
t1 = time.clock()
merge_sort(l, 0, len(l)-1)
t2 = time.clock()
print("MERGE(10K): ", t2 - t1)

l = random_list(0, 100000, 100000)
t1 = time.clock()
merge_sort(l, 0, len(l)-1)
t2 = time.clock()
print("MERGE(100K): ", t2 - t1)

l = random_list(0, 1000000, 1000000)
t1 = time.clock()
merge_sort(l, 0, len(l)-1)
t2 = time.clock()
print("MERGE(1M): ", t2 - t1)