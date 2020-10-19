
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

def recursive_insertion_sort(A, n):
    if n <= 1:
        return

    recursive_insertion_sort(A, n-1)
    key = A[n - 1]
    j = n - 2
    while j >= 0 and A[j] >= key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
recursive_insertion_sort(arr, len(arr))
#insertion_sort(arr)
print(arr)