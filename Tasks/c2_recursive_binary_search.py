from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, left_border = None, right_border = None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    # left_border = 0
    # right_border = len(arr) - 1

    middle_index = left_border + (right_border - left_border) // 2
    middle_elem = arr[middle_index]

    if middle_elem == elem:
        return middle_index
    if left_border >= right_border:
        return None

    if middle_elem < elem:
        new_left_border = middle_index + 1
        return binary_search(elem, arr, new_left_border, right_border)


    if middle_elem > elem:
        new_right_border = middle_index - 1
        return binary_search(elem, arr, left_border, new_right_border)



#
if __name__ == '__main__':
    arr = [i for i in range(10)]
    print(arr)
    print(binary_search(5, arr))
