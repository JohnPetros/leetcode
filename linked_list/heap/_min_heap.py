from math import log
from typing import Any


class MinHeap:
    def __init__(self) -> None:
        self._nodes_count = 0
        self._heap = []

    def push(self, new_node) -> None:
        self._heap.append(new_node)
        self._nodes_count += 1

        node_index = self._nodes_count

        while True:
            if node_index == 1:
                break

            parent_node_index = node_index // 2
            if self._heap[parent_node_index - 1] <= self._heap[node_index - 1]:
                break
            else:
                self._heap[parent_node_index - 1], self._heap[node_index - 1] = (
                    self._heap[node_index - 1],
                    self._heap[parent_node_index - 1],
                )
                node_index = parent_node_index

    def pop(self) -> Any:
        if self._nodes_count < 1:
            raise IndexError("Empty Heap")

        root = self._heap[0]
        self._heap[0] = self._heap[self._nodes_count - 1]
        self._heap.pop()
        self._nodes_count -= 1

        parent_node_index = 1
        while True:
            node_index = parent_node_index * 2
            if node_index > self._nodes_count:
                break

            if node_index + 1 <= self._nodes_count:
                if self._heap[node_index + 1 - 1] < self._heap[node_index - 1]:
                    node_index += 1

            if self._heap[parent_node_index - 1] <= self._heap[node_index - 1]:
                break
            else:
                (
                    self._heap[parent_node_index - 1],
                    self._heap[node_index - 1],
                ) = (
                    self._heap[node_index - 1],
                    self._heap[parent_node_index - 1],
                )
                parent_node_index = node_index

        return root

    def peek(self) -> Any:
        if self._nodes_count == 0:
            raise IndexError("Empty heap")

        return self._heap[0]

    def left_child(self, index: int) -> Any:
        left_child_index = 2 * (index + 1)

        if self._nodes_count < left_child_index:
            raise IndexError("Left child not found")

        return self._heap[left_child_index - 1]

    def right_child(self, index: int) -> Any:
        right_child_index = 2 * (index + 1) + 1

        if self._nodes_count < right_child_index:
            raise IndexError("Right child not found")

        return self._heap[right_child_index - 1]

    def parent(self, index: int) -> Any:
        return self._heap[index // 2]

    def __rpr__(self) -> str:
        if self._nodes_count == 0:
            raise IndexError("Empty heap")

        last_level = int(log(self._nodes_count, 2))
        node_index = 0
        rpr = ""

        for level in range(last_level):
            for _ in range(2**level):
                rpr += f"{self._heap[node_index]} "
                node_index += 1
            rpr += "\n"

        for _ in range(self._nodes_count - node_index):
            rpr += f"{self._heap[node_index]} "
            node_index += 1

        return rpr

    def __str__(self) -> str:
        return self.__rpr__()

    def __len__(self) -> int:
        return self._nodes_count

    def __bool__(self) -> bool:
        return bool(self._nodes_count)
