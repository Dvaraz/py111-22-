"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    EPSILON = 0.000000001
    sum = 0
    n = 0
    while True:
        k = (x ** n) / (math.factorial(n))
        n += 1
        sum += k
        if k < EPSILON:
            return sum


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)
    return 0

if __name__ == '__main__':
    x = 1.553
    n = 1
    s = 0
    for i in range(10):
        k = (x ** n) / (math.factorial(n))
        n += 1
        s += k

