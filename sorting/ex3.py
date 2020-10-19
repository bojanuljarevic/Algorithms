import random
import time
from merge import *
from quicksort import *

l1 = []
for i in range(0, 1000):
    l1.append(random.randint(0, 1000))


print(l1)
t1 = time.clock()
merge_sort(l1, 0, len(l1)-1)
t2 = time.clock()
t = t2 - t1
print(l1)
print("Merge sort(1000):")
print(t)

l2 = []
for i in range(0, 1000):
    l2.append(random.randint(0, 1000))

print(l2)
t1 = time.clock()
randomized_quicksort(l2, 0, len(l2)-1)
t2 = time.clock()
t = t2 - t1
print(l2)
print("Quick sort(1000):")
print(t)


l3 = []
for i in range(0, 1000000):
    l3.append(random.randint(0, 1000000))

#print(l3)
t1 = time.clock()
merge_sort(l3, 0, len(l3)-1)
t2 = time.clock()
t = t2 - t1
#print(l3)
print("Merge sort(1000000):")
print(t)

l4 = []
for i in range(0, 1000000):
    l4.append(random.randint(0, 1000000))

#print(l4)
t1 = time.clock()
randomized_quicksort(l4, 0, len(l4)-1)
t2 = time.clock()
t = t2 - t1
#print(l4)
print("Quick sort(1000000):")
print(t)

