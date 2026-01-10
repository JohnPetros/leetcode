class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


def reverse_linked_list(head: ListNode):
    current = head
    previous = None

    while current:
        temporary = current.next
        current.next = previous
        previous = current
        current = temporary

    return previous
    # Time (N)
    # Space (1)


print(
    reverse_linked_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
)
