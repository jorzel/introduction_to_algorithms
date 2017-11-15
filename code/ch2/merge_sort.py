

def merge(right, left):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0

    while(True):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result


def merge_sort(A):
    if len(A) < 2:
        return A

    middle = len(A) / 2
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left, right)

A = [31, 1, 59, 76, 41, 98, 66]

