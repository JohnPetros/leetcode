from _node import Node
from _linked_list import LinkedList


def swap_nodes_in_pairs(head: Node):
    dummy_node = Node()
    dummy_node.next = head
    current_node = dummy_node

    while current_node.next and current_node.next.next:
        first_node = current_node.next
        second_node = current_node.next.next

        first_node.next = second_node.next
        second_node.next = first_node
        current_node.next = second_node

        current_node = current_node.next.next

    return dummy_node.next


list = LinkedList(1, 2, 3, 4)
print(swap_nodes_in_pairs(list.head))
