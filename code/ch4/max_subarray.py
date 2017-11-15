import sys


def max_crossing_subarray(A, low, mid, high):
    left_sum, right_sum = -sys.maxint, -sys.maxint
    sum_ = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sum_ = sum_ + A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i
    sum_ = 0
    max_right = mid
    for i in range(mid + 1, high + 1):
        sum_ = sum_ + A[i]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = i
    return max_left, max_right, left_sum + right_sum


def max_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (high + low) // 2
        left_low, left_high, left_sum = max_subarray(A, low, mid)
        right_low, right_high, right_sum = max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


A = [31, -41, -59, 26, -25, -3, 1, 58, -1, 1, 7]
print max_subarray(A, 0, len(A) - 1)