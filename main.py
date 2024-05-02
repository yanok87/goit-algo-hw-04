import timeit


numbers = [5, 3, 8, 4, 2]


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


execution_time_insertion = timeit.timeit(lambda: insertion_sort(numbers), number=1000)
print("insertion_sort", execution_time_insertion)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
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


execution_time_merge = timeit.timeit(lambda: merge_sort(numbers), number=1000)
print("merge_sort", execution_time_merge)


def timsort(arr):
    sorted_arr = arr.sort()
    return sorted_arr


execution_time_timsort = timeit.timeit(lambda: timsort(numbers), number=1000)
print("timsort", execution_time_timsort)
