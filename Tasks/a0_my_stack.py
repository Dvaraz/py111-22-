"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        print(elem)
        self.stack.append(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        if ind == 0:
            return self.stack[-1]
        elif ind > len(self.stack):
            return None
        else:
            return self.stack[-ind - 1]

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.stack.clear()
        return None


if __name__ == '__main__':
    pass