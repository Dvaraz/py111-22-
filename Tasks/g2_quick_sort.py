from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if not container:
        return container

    def _sort(left_border, right_border):
        if len(container[left_border:right_border]) == 1 or len(container[left_border:right_border]) == 0:
            return None
        random_index = random.randint(left_border, right_border)
        pivot = container[right_border]
        i = left_border - 1
        j = left_border
        for k in range(len(container[left_border: right_border + 1])):
            if container[j] <= pivot:
                i += 1
                container[i], container[j] = container[j], container[i]
            j += 1

        _sort(left_border, i - 1)
        _sort(i, right_border)

    _sort(0, len(container) - 1)
    return container
    # def _sort(left_border, right_border):
    #     if left_border >= right_border:
    #         return
    #     random_index = random.randint(left_border, right_border)
    #     pivot = container[random_index]
    #
    #     i, j = left_border, right_border
    #
    #     while i <= j:
    #         while container[i] < pivot:
    #             i += 1
    #
    #         while container[j] > pivot:
    #             j -= 1
    #
    #         if i <= j:
    #             container[i], container[j] = container[j], container[i]
    #             i += 1
    #             j -= 1
    #     _sort(left_border, j)
    #     _sort(i, right_border)
    # _sort(0, len(container) - 1)
    # return container


# if __name__ == '__main__':
#     # arr = [random.randint(0, 10) for _ in range(6)]
#     arr = [10, 80, 30, 90, 40, 50, 70]
#     # arr = [random.randint(-100, 100) for _ in range(30)]
#     # print(sorted(arr))
#     # print(sort(arr))