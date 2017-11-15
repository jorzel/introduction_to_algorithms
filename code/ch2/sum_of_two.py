from insertion_sort import insertion_sort
from merge_sort import merge


def dedupe(S):
    added = []
    for s in S:
        if s not in added:
            added.append(s)
    return added


def sum_of_two(table, x):
    insertion_sort(table)
    table = dedupe(table)
    diff = [x - y for y in table]
    insertion_sort(diff)
    diff = dedupe(diff)
    merged = merge(table, diff)
    for i in range(len(merged) - 1):
        if merged[i] == merged[i + 1]:
            return merged[i], x - merged[i]
    return None

A = [31, 41, 59, 26, 58, 1, 7]

print sum_of_two(A, 72)
