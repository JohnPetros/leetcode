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


def add_two_numbers(head_1, head_2):
    dummy = ListNode()
    head = dummy
    carry = 0

    while head_1 or head_2 or carry:
        value_1 = head_1.value if head_1 else 0
        value_2 = head_2.value if head_2 else 0

        sum = value_1 + value_2 + carry
        digit = sum % 10
        carry = sum // 10

        head.next = ListNode(digit)
        head = head.next

        head_1 = head_1.next if head_1 else None
        head_2 = head_2.next if head_2 else None

    return dummy.next


head_1 = ListNode(2, ListNode(4, ListNode(3)))
head_2 = ListNode(5, ListNode(6, ListNode(4)))

print(add_two_numbers(head_1, head_2))
