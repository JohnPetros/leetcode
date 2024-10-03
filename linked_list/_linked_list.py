from typing import Any

from _node import Node


class LinkedList:
    def __init__(self, *values: list[Any]) -> None:
        self.head = None
        self._size = 0

        for value in values:
            self.append(value)

    def append(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        pointer = self.head

        while pointer.next:
            pointer = pointer.next

        pointer.next = Node(value)
        self._size += 1

    def insert(self, index: int, value: Any):
        node = Node(value)

        if index == 0:
            node.next = self.head
            self.head = node
            return

        pointer = self.__get_node(index - 1)
        node.next = pointer.next
        pointer.next = node
        self._size += 1

    def remove(self, value: Any):
        if self.head is None:
            raise ValueError(f"{value} not found in the list")

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return

        previous = self.head
        pointer = self.head.next

        while pointer:
            if pointer.value == value:
                previous.next = pointer.next
                pointer.next = None
                self._size -= 1
                return

            previous = pointer
            pointer = pointer.next

        raise ValueError(f"{value} not found in the list")

    def index(self, value: Any):
        pointer = self.head
        index = 0

        while pointer:
            if pointer.value == value:
                return index

            pointer = pointer.next
            index += 1

        raise ValueError(f"{value} not found in the list")

    def min(self) -> int:
        if self.head is None:
            raise ValueError("List is empty")

        pointer = self.head
        min_value = pointer.value

        while pointer:
            if pointer.value < min_value:
                min_value = pointer.value
            pointer = pointer.next

        return min_value

    def reverse(self) -> None:
        previous = self.head.next
        next = self.head.next
        self.head.next = None

        while previous:
            previous = previous.next
            next.next = self.head
            self.head = next
            next = previous

    def __get_node(self, index: int) -> Node:
        pointer = self.head

        for _ in range(index):
            if not pointer:
                raise IndexError("Index out of range")

            pointer = pointer.next

        if not pointer:
            raise IndexError("Index out of range")
        return pointer

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int):
        return self.__get_node(index)

    def __setitem__(self, index: int, value: Any):
        pointer = self.__get_node(index)
        pointer.value = value

    def __repr__(self) -> str:
        pointer = self.head
        repr = ""

        while pointer:
            repr += f"{pointer.value} -> "
            pointer = pointer.next

        return repr[:-4]

    def __str__(self) -> str:
        return self.__repr__()


head = LinkedList(1, 2, 3).head
node1 = Node(4)
node2 = Node(5)

node1 = head.next
head.next = 5
print(node1)
