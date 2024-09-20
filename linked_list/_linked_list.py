from linked_list._node import Node


class LinkedList:
    def __init__(self, *values) -> None:
        self.head = None

        for value in values:
            self.append(value)

    def append(self, value) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        pointer = self.head

        while pointer.next:
            pointer = pointer.next

        pointer.next = Node(value)

    def __repr__(self) -> str:
        pointer = self.head
        repr = ""

        while pointer:
            repr += f"{pointer.value} -> "
            pointer = pointer.next

        return repr[:-4]
