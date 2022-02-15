from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left_border = 0
    right_border = len(arr) - 1
    while left_border <= right_border:
        middle_index = left_border + (right_border - left_border) // 2
        middle_elem = arr[middle_index]
        if middle_elem == elem:
            return middle_index

        if middle_elem < elem:
            left_border = middle_index + 1

        if middle_elem > elem:
            right_border = middle_index - 1


if __name__ == '__main__':
    arr = [i for i in range(1, 101)]
    print(arr)
    print(binary_search(-1, arr))
