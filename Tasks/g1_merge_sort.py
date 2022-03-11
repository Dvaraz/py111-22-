from typing import List
import random


def merge_func(sorted_left, sorted_right):
    arr = []
    l = r = 0
    while l < len(sorted_left) and r < len(sorted_right):
        if sorted_left[l] < sorted_right[r]:
            arr.append(sorted_left[l])
            l += 1
        else:
            arr.append(sorted_right[r])
            r += 1

    while l < len(sorted_left):
        arr.append(sorted_left[l])
        l += 1
    while r < len(sorted_right):
        arr.append(sorted_right[r])
        r += 1
    return arr


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container

    mid = len(container) // 2

    left = sort(container[:mid])
    right = sort(container[mid:])

    return merge_func(left, right)


if __name__ == '__main__':
    arr = [random.randint(0, 10) for _ in range(6)]
    print(arr)
    print(sort(arr))