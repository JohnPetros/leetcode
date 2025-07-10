class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        current = self
        nodes = []
        while current:
            nodes.append(str(current.value))
            current = current.next
        return " -> ".join(nodes)


def remove_nth_node_from_end_of_list(head: ListNode, nth: int) -> ListNode:
    dummy_head = ListNode()
    dummy_head.next = head
    fast_head = dummy_head
    slow_head = dummy_head

    for _ in range(nth + 1):
        fast_head = fast_head.next

    while fast_head is not None:
        fast_head = fast_head.next
        slow_head = slow_head.next

    slow_head.next = slow_head.next.next
    return dummy_head.next
    # O(n) time complexity
    # O(1) space complexity


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(remove_nth_node_from_end_of_list(head, 2))
