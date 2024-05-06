"""This module compares three different sorting algorythms"""

import timeit
import random


# Creation of three different arrays of numbers
unsorted_array = [random.randint(1, 100) for _ in range(100)]
sorted_array = sorted(unsorted_array)
A = sorted_array[: len(sorted_array) // 2]
B = sorted_array[len(sorted_array) // 2 :]
partially_sorted_array = B + A


def insertion_sort(lst):
    """This function implements the Insertion sort"""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


insertion_unsorted = timeit.timeit(lambda: insertion_sort(unsorted_array), number=1000)
print("insertion_unsorted:", insertion_unsorted)

insertion_partially_sorted = timeit.timeit(
    lambda: insertion_sort(partially_sorted_array), number=1000
)
print("insertion_partially_sorted:", insertion_partially_sorted)

insertion_sorted = timeit.timeit(lambda: insertion_sort(sorted_array), number=1000)
print("insertion_sorted:", insertion_sorted)


def merge_sort(arr):
    """This function implements the Merge sort"""

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    """This function implements the auxiliary merge of arrays"""

    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


merge_unsorted = timeit.timeit(lambda: merge_sort(unsorted_array), number=1000)
print("merge_unsorted:", merge_unsorted)

merge_partially_sorted = timeit.timeit(
    lambda: merge_sort(partially_sorted_array), number=1000
)
print("merge_partially_sorted:", merge_partially_sorted)

merge_sorted = timeit.timeit(lambda: merge_sort(sorted_array), number=1000)
print("merge_sorted:", merge_sorted)


def timsort(arr):
    """This function uses the inbuilt Timsort algorythm"""

    sorted_arr = arr.sort()
    return sorted_arr


timsort_unsorted = timeit.timeit(lambda: timsort(unsorted_array), number=1000)
print("timsort_unsorted:", timsort_unsorted)

timsort_partially_sorted = timeit.timeit(
    lambda: timsort(partially_sorted_array), number=1000
)
print("timsort_partially_sorted:", timsort_partially_sorted)

timsort_sorted = timeit.timeit(lambda: timsort(sorted_array), number=1000)
print("timsort_sorted:", timsort_sorted)

"""ANALYSIS: ⁠For unsorted arrays: Timsort outperforms both Incertion and Merge sort.````
⁠For partially sorted arrays: Timsort still has the lowest execution time, followed closely by Incertion and then Merge sort.
⁠For sorted arrays: Timsort remains the fastest, with Insertion slightly slower, and Merge sort being the slowest among the three."""
