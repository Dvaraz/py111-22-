"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priority_queue = {}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        complexity O(1)
        """
        # if priority not in self.priority_queue.keys():
        #     self.priority_queue[priority] = []
        # self.priority_queue[priority] += [elem]
        self.priority_queue[priority] = self.priority_queue.get(priority, [])
        self.priority_queue[priority].append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        complexity O(k)
        """
        if not self.priority_queue:
            return None
        high_priority_key = min(self.priority_queue)
        a = self.priority_queue[high_priority_key].pop(0)
        if not self.priority_queue[high_priority_key]:
            del self.priority_queue[high_priority_key]
        return a

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        complexity O(k)
        """
        if self.priority_queue:
            return self.priority_queue[priority][ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priority_queue.clear()
        return None


if __name__ == '__main__':
    priority_queue = PriorityQueue()

    high_priority = 0
    medium_priority = 5
    low_priority = 10
    priority_queue.enqueue(3, medium_priority)
    # priority_queue.enqueue(5, medium_priority)
    # priority_queue.enqueue(7, medium_priority)

    priority_queue.enqueue(10, high_priority)
    priority_queue.enqueue(0, low_priority)

    print(priority_queue.priority_queue)

