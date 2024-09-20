from typing import Optional

from _linked_list import LinkedList
from _node import Node


def add_two(list_1_node: Optional[Node], list_2_node: Optional[Node]) -> Optional[Node]:
    head = Node(0)
    pointer = head
    exceed = 0

    while list_1_node or list_2_node or exceed:
        value_1 = list_1_node.value if list_1_node else 0
        value_2 = list_2_node.value if list_2_node else 0

        sum = value_1 + value_2 + exceed
        digit = sum % 10
        exceed = sum // 10

        pointer.next = Node(digit)
        pointer = pointer.next

        list_1_node = list_1_node.next if list_1_node else None
        list_2_node = list_2_node.next if list_2_node else None

    return head.next


list_1 = LinkedList(2, 4, 3)
list_2 = LinkedList(5, 6, 4)

print(add_two(list_1.head, list_2.head))
