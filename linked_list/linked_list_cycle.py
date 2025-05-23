class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
    # Time Complexity: O(n)
    # Space Complexity: O(1)


print(
    linked_list_cycle(ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))),
    linked_list_cycle(ListNode(1, ListNode(2, ListNode(1)))),
)
