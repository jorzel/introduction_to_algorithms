
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while (i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def recursive_insertion_sort(A, n):
    if n <= 1:
        return

    recursive_insertion_sort(A, n - 1)
    last = A[n - 1]
    i = n - 2
    while (i >= 0 and A[i] > last):
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = last
    return A


def search_in(A, v):
    for i in range(len(A)):
        if v == A[i]:
            return i
    return -1


A = [31, 41, 59, 26, 41, 58, 1, 7]
