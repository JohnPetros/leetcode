from _linked_list import LinkedList
from node import Node


def remove_nth_node_from_end_of_list(head_node: Node, nth: int) -> Node:
    dummy_node = Node()
    dummy_node.next = head_node
    behind_node = dummy_node
    ahead_node = dummy_node

    for _ in range(nth + 1):
        ahead_node = ahead_node.next

    while ahead_node:
        behind_node = behind_node.next
        ahead_node = ahead_node.next

    behind_node.next = behind_node.next.next

    return head_node


list = LinkedList(0, 2, 4, 6, 8, 10)

print(remove_nth_node_from_end_of_list(list.head, 3))
