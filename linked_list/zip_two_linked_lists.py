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


def zip_two_linked_lists(first_head: ListNode, second_head: ListNode) -> ListNode:
    dummy = first_head

    while first_head and second_head:
        first_temporary_head = first_head.next
        second_temporary_head = second_head.next

        first_head.next = second_head
        second_head.next = first_temporary_head

        first_head = first_temporary_head
        second_head = second_temporary_head

    return dummy


first_head = ListNode(5, ListNode(4, ListNode(3)))
second_head = ListNode(1, ListNode(2, ListNode(3)))

print(f"Primeira Lista Original: {first_head}")
print(f"Segunda Lista Original: {second_head}")

interleaved_list_head = zip_two_linked_lists(first_head, second_head)

print(f"Lista Intercalada: {interleaved_list_head}")
