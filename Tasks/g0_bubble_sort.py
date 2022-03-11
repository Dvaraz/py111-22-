from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    size = len(container)
    for i in range(size):
        for j in range(0, size - i - 1):
            if container[j] > container[j + 1]:
                container[j + 1], container[j] = container[j], container[j + 1]

    return container


