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
        if priority not in self.priority_queue:
            self.priority_queue[priority] = []
        self.priority_queue[priority] += [elem]
        # queue = self.priority_queue.get(priority, [])
        # queue.append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        complexity O(k)
        """
        # self.priority_queue = dict(sorted(self.priority_queue.items()))
        # -----
        # if not self.priority_queue:
        #     return None
        # local_high_priority = min(self.priority_queue)
        # queue = self.priority_queue[high_priority]
        # return_value = queue.pop()
        # if not queue:
        #     del self.priority_queue[local_high_priority]
        # del self.priority_queue["key"]
        # -----
        if not self.priority_queue:
            return None
        if self.priority_queue[0] != []:
            return self.priority_queue[0].pop(0)
        elif self.priority_queue[5] != []:
            return self.priority_queue[5].pop(0)
        else:
            return self.priority_queue[10].pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        complexity O(k)
        """
        if self.priority_queue:
            if priority == 0:
                return self.priority_queue[0][ind]
            elif priority == 5:
                return self.priority_queue[5][ind]
            elif priority == 10:
                return self.priority_queue[10][ind]

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
    priority_queue.enqueue(5, medium_priority)
    priority_queue.enqueue(7, medium_priority)

    priority_queue.enqueue(10, high_priority)
    priority_queue.enqueue(0, low_priority)

    priority_queue.priority_queue = dict(sorted(priority_queue.priority_queue.items()))
    print(priority_queue.priority_queue)

    for key, value in priority_queue.priority_queue.items():
        print(key, value)