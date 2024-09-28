from _node import Node
from _linked_list import LinkedList


def swap_nodes_in_pairs(head: Node, k: int) -> Node:
    def reverse(head: Node, k: int):
        previous_node = None
        current_node = head

        for _ in range(k):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node

    def get_length(node: Node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    length = get_length(head)
    dummy_node = Node()
    dummy_node = head
    previous_group_end = head

    while length >= k:
        group_start = previous_group_end.next
        group_end = group_start
        for _ in range(k - 1):
            group_end = group_end.next

        next_group_start = group_end.next
        group_end.next = None
        previous_group_end.next = reverse(group_start, k)
        group_start.next = next_group_start
        length -= k

    return dummy_node.next


list = LinkedList(1, 2, 3, 4, 6)
print(swap_nodes_in_pairs(list.head, 6))
