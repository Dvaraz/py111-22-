from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    # if not container:
    #     return container
    # pivot = random.choice(container)
    #
    # return sort([v for v in container if v < pivot]) \
    #             + [v for v in container if v == pivot] \
    #             + sort([v for v in container if v > pivot])
    # pivot = container[-1]
    # print(pivot)
    # i = 0
    # for j in range(len(container)):
    #     if container[j] <= pivot:
    #         container[i], container[j] = container[j], container[i]
    #         i += 1
    #
    # return container
    def _sort(left_border, right_border):
        if left_border >= right_border:
            return
        random_index = random.randint(left_border, right_border)
        pivot = container[random_index]

        i, j = left_border, right_border

        while i <= j:
            while container[i] < pivot:
                i += 1

            while container[j] > pivot:
                j -= 1

            if i <= j:
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1
        _sort(left_border, j)
        _sort(i, right_border)
    _sort(0, len(container) - 1)
    return container


if __name__ == '__main__':
    # arr = [random.randint(0, 10) for _ in range(6)]
    arr = [10, 80, 30, 90, 40, 50, 70]
    print(sort(arr))