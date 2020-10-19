
import random
import time

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

#Zadatak sa vjezbi - implementacija

def parent(i):
    return i // 2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, i, heapsize):
    l = left(i)
    r = right(i)
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heapsize)

def build_max_heap(A):
    for i in range(len(A)//2 - 1, -1, -1):
        max_heapify(A, i, len(A))

def heapsort(A):
    build_max_heap(A)
    heapsize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        max_heapify(A, 0, heapsize)


# Zadatak sa predavanje - implementacija
def heap_delete(A, i):
    A[i], A[-1] = A[-1], A[i]               # const             postavljanje elementa koji treba izbaciti na kraj
    heapsize = len(A) - 1                   # const             da ne bismo uzimali element koji cemo izbaciti u obzir tokom popravljanja heapa
    max_heapify(A, i, heapsize)             # T(n) = lg(n)      popravljanje heapa
    A.pop(-1)                               # const             izbacivanje elementa sa kraja

# Ukupna slozenost: O(n) = lg(n) + c1 + c2 + c3 = lg(n)

def heap_insert(A, n):
    A.append(n)
    build_max_heap(A)

l = random_list(0, 1000, 10)

# Zadatak sa predavanja - testiranje

print("BRISANJE ELEMENTA:")
print("Inicijalni niz:")
print(l)
build_max_heap(l)
print("Heap:")
print(l)
heap_delete(l, 5)
print("Uklanjanje elementa:")
print(l)
print("\n")

# Zadatak sa vjezbi - testiranje

l = random_list(0, 100, 100)
print("HEAPSORT(100):")
t1 = time.clock()
print("Inicijalni niz: ", l)
heapsort(l)
print("Sortirani niz: ", l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 1000, 1000)
print("HEAPSORT(1K):")
t1 = time.clock()
heapsort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 10000, 10000)
print("HEAPSORT(10K):")
t1 = time.clock()
heapsort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 100000, 100000)
print("HEAPSORT(100K):")
t1 = time.clock()
heapsort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

l = random_list(0, 1000000, 1000000)
print("HEAPSORT(1M):")
t1 = time.clock()
heapsort(l)
t2 = time.clock()
print("Trajanje: ", t2 - t1)

