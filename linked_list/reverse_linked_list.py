class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


def reverse_linked_list(head: ListNode):
    current_node = head
    previous_node = None

    while current_node:
        temporary_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = temporary_node

    return previous_node


print(
    reverse_linked_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
)
