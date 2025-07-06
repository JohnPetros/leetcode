class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


def middle_of_linked_list(head: ListNode):
    ahead = head

    while ahead and ahead.next:
        ahead = ahead.next.next
        head = head.next

    return head
    # Time complexity: O(n)
    # Space complexity: O(1)


print(
    middle_of_linked_list(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    )
)
