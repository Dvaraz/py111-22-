from typing import Union, Sequence


def stairway_path2(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    count_stairs = len(stairway)
    total_cost = [0] * count_stairs
    print(stairway)
    total_cost[0] = stairway[0]
    total_cost[1] = stairway[1]
    for i in range(2, len(stairway)):
        total_cost[i] = stairway[i] + min(total_cost[i - 1], total_cost[i - 2])

    return total_cost[-1]

def stairway_path3(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    count_stairs = len(stairway)
    total_cost: list[float] = [float("inf")] * count_stairs
    total_cost[0] = stairway[0]
    total_cost[1] = stairway[1]
    for i in range(0, len(stairway) - 2):
        total_cost[i + 1] = min(stairway[i + 1] + total_cost[i], total_cost[i + 1])
        total_cost[i + 2] = min(stairway[i + 2] + total_cost[i], total_cost[i + 2])
    total_cost[-1] = min(stairway[-1] + total_cost[-2], total_cost[-1])
    print(total_cost)
    return total_cost[-1]


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    total_cost = {

    }
    def lazy_stairway_path(stair_number: int):
        # i = min(i - 1, i - 2)
        if stair_number in total_cost:
            return total_cost[stair_number]

        if stair_number == 0:
            total_cost[stair_number] = stairway[stair_number]
            return stairway[stair_number]
        if stair_number == 1:
            total_cost[stair_number] = stairway[stair_number]
            return stairway[stair_number]
        total_cost[stair_number] = stairway[stair_number] + min(lazy_stairway_path(stair_number - 1), lazy_stairway_path(stair_number - 2))
        return total_cost[stair_number]
    return lazy_stairway_path(len(stairway) - 1)


if __name__ == '__main__':
    test_st = [5, 11, 43, 2, 23, 43, 22, 12, 6, 8]  # 26
    print(stairway_path(test_st))
    # for i in range(2, len(test_st)):
    #     print(test_st[i])