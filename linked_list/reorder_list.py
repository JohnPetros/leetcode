class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


def reorder_list(head):
    if not head:
        return

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow
    previous = None
    while second:
        temporary = second.next
        second.next = previous
        previous = second
        second = temporary

    first = head  # 1 -> 2 -> 3 -> 4 -> 5 -> None
    second = previous  # 5 -> 4 -> 3 -> None

    while second:
        first_temporary = first.next  # 2 -> 3 -> 4 -> 5 -> None
        second_temporary = second.next  # 4 -> 3 -> None

        first.next = second  # 1 -> 5 -> 2
        second.next = first_temporary  # 5 -> 2 -> 3

        first = first_temporary  # 2
        second = second_temporary  # 4

    return head


print(reorder_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
