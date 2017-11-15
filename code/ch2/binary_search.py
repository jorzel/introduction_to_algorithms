

def binary_search(A, v, start, end):
    middle = (start + end) / 2

    if A[middle] == v:
        return middle
    if (end - start) == 1:
        return -1
    else:
        if v < A[middle]:
            return binary_search(A, v, start, middle)
        elif v > A[middle]:
            return binary_search(A, v, middle + 1, end)

A = [31, 41, 59, 26, 41, 58, 1, 7]

