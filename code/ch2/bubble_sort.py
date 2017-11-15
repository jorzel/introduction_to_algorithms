

def bubble_sort(A):
    len_ = len(A)
    for i in range(len_ - 1):
        for j in reversed(xrange(i + 1, len_)):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A


A = [31, 41, 59, 26, 41, 58, 4, 2]
