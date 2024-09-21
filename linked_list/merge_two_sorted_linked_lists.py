from _node import Node
from _linked_list import LinkedList


def merge_two_sorted_linked_lists(node_1: Node, node_2: Node) -> Node:
    dummy = Node()
    sorted_linked_list = dummy

    while node_1 and node_2:
        if node_1.value < node_2.value:
            sorted_linked_list.next = node_1
            sorted_linked_list = node_1
            node_1 = node_1.next
        else:
            sorted_linked_list.next = node_2
            sorted_linked_list = node_2
            node_2 = node_2.next

    if node_1:
        sorted_linked_list.next = node_1
    if node_2:
        sorted_linked_list.next = node_2

    return dummy.next


linked_list_1 = LinkedList(1, 2, 4)
linked_list_2 = LinkedList(1, 3, 4)

print(merge_two_sorted_linked_lists(linked_list_1.head, linked_list_2.head))

# linked_list_1 = LinkedList()
# linked_list_2 = LinkedList()
# print(merge_two_sorted_linked_lists(linked_list_1.head, linked_list_2.head))
