

def selection_sort(A):
    for i in range(len(A) - 1):
        key = A[i]
        _min, _ind = min_val(A[i:])
        A[i] = _min
        A[i + _ind] = key
    return A


def min_val(A):
    if A[0]:
        _min = A[0]
        _ind = 0
    else:
        return -1

    for i in xrange(1, len(A)):
        if _min > A[i]:
            _min = A[i]
            _ind = i
    return _min, _ind


A = [31, 41, 59, 26, 41, 58]

print selection_sort(A)