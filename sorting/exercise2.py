import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def insertion_sort(A):
  for j in range(1,len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
      A[i+1] = A[i]
      i = i - 1
    A[i+1] = key

def bubble_sort(A):
  for i in range(0, len(A)-1):
    for j in range(i+1, len(A)):
      if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]

def linear_search(A, key):
  for i in range(0, len(A)):
    if A[i] == key :
      return i
  return None

def binary_search(A, key):
  insertion_sort(A)
  min = 0
  max = len(A)
  while min <= max:
    mid = (min + max) // 2
    if key > A[mid]:
      min = mid + 1
    elif key < A[mid]:
      max = mid - 1
    else:
      return mid
  return None

def recursive_binary_search(A, key, min, max):
    # it is expected that the list is sorted beforehand
    mid = (max + min) // 2
    if key == A[mid]:
      print(mid)
      return mid
    elif min >= max or mid == max or mid == min:
      print(None)
      return None
    elif A[mid] < key:
      recursive_binary_search(A, key, mid, max)
    else:
      recursive_binary_search(A, key, min, mid)



l = random_list(0, 101, 100)
t1 = time.clock()
bubble_sort(l)
t2 = time.clock()
print("BUBBLE SORT(100): ", t2 - t1)

l = random_list(0, 101, 100)
t1 = time.clock()
insertion_sort(l)
t2 = time.clock()
print("INSERTION SORT(100): ", t2 - t1)


l = random_list(0, 1001, 1000)
t1 = time.clock()
bubble_sort(l)
t2 = time.clock()
print("BUBBLE SORT(1K): ", t2 - t1)

l = random_list(0, 1001, 1000)
t1 = time.clock()
insertion_sort(l)
t2 = time.clock()
print("INSERTION SORT(1K): ", t2 - t1)

l = random_list(0, 10001, 10000)
t1 = time.clock()
bubble_sort(l)
t2 = time.clock()
print("BUBBLE SORT(10K): ", t2 - t1)

l = random_list(0, 10001, 10000)
t1 = time.clock()
insertion_sort(l)
t2 = time.clock()
print("INSERTION SORT(10K): ", t2 - t1)

l = random_list(0, 100001, 100000)
t1 = time.clock()
bubble_sort(l)
t2 = time.clock()
print("BUBBLE SORT(100K):", t2 - t1)

l = random_list(0, 100001, 100000)
t1 = time.clock()
insertion_sort(l)
t2 = time.clock()
print("INSERTION SORT(100K): ", t2 - t1)




