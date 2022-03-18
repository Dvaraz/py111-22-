def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    # point(i, j) = point(i - 2, j + 1) + point(i - 2, j - 1) + point(i - 1, j - 2) + point(i + 1, j - 2)
    rows = shape[0]
    cols = shape[1]
    print(rows, cols)
    def step(i, j):
        if i == 0 and j == 0:
            return 1
        if 0 >= i <= rows:
            return 0
        if 0 >= j <= cols:
            return 0
        return step(i - 2, j + 1) + step(i - 2, j - 1) + step(i - 1, j - 2) + step(i + 1, j - 2)
    return step(point[0], point[1])


if __name__ == '__main__':
    print(calculate_paths((4, 4), (4, 4)))
