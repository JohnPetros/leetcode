class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        current = self
        nodes = []
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)


def reorder_list(head):
    # find middle
    slow_head, fast_head = head, head.next
    while fast_head and fast_head.next:
        slow_head = slow_head.next
        fast_head = fast_head.next.next

    # reverse second half
    second_half_head = slow_head.next
    inverted_second_half_head = slow_head.next = None
    while second_half_head:
        temporary_head = second_half_head.next
        second_half_head.next = inverted_second_half_head
        inverted_second_half_head = second_half_head
        second_half_head = temporary_head

    # zip two halfs
    first_half_head, second_half_head = head, inverted_second_half_head
    while second_half_head:
        tmp1, tmp2 = first_half_head.next, second_half_head.next
        first_half_head.next = second_half_head
        second_half_head.next = tmp1
        first_half_head, second_half_head = tmp1, tmp2

    return head
    # O(n) time complexity
    # O(1) space complexity


print(reorder_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))))
print(reorder_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
