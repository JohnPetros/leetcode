from typing import Any
from _node import Node


class Stack:
    def __init__(self) -> None:
        self._top = None
        self._size = 0

    def push(self, value: Any) -> None:
        node = Node(value)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self) -> Any:
        if self._size == 0:
            raise IndexError("Stack is empty")

        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.value

    def peek(self) -> Any:
        if self._size == 0:
            raise IndexError("Stack is empty")

        return self._top.value

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        if self._size == 0:
            return "Empty"

        repr = ""
        node = self._top

        while node:
            repr += str(node.value) + "\n"
            node = node.next
            if node:
                repr += "↓\n"

        return repr

    def __str__(self) -> str:
        return self.__repr__()
