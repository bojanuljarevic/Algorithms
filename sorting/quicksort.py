#!/usr/bin/python

import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)



l = random_list(0, 100, 100)
t1 = time.clock()
randomized_quicksort(l, 0, len(l)-1)
t2 = time.clock()
print("QUICK(100): ", t2 - t1)

l = random_list(0, 1000, 1000)
t1 = time.clock()
randomized_quicksort(l, 0, len(l)-1)
t2 = time.clock()
print("QUICK(1K): ", t2 - t1)

l = random_list(0, 10000, 10000)
t1 = time.clock()
randomized_quicksort(l, 0, len(l)-1)
t2 = time.clock()
print("QUICK(10K): ", t2 - t1)

l = random_list(0, 100000, 100000)
t1 = time.clock()
randomized_quicksort(l, 0, len(l)-1)
t2 = time.clock()
print("QUICK(100K): ", t2 - t1)

l = random_list(0, 1000000, 1000000)
t1 = time.clock()
randomized_quicksort(l, 0, len(l)-1)
t2 = time.clock()
print("QUICK(1M): ", t2 - t1)