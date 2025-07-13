class Node:
    def __init__(self, value=0, next=None, random=None):
        self.value = value
        self.next = next
        self.random = random

    def __str__(self) -> str:
        current = self
        nodes = []
        while current:
            nodes.append(str(current.value))
            current = current.next
        return " -> ".join(nodes)


def copy_list_with_random_pointer(head: Node):
    if not head:
        return None

    nodes_map = dict()

    head_copy = head
    while head_copy:
        node = Node(head_copy.value)
        nodes_map[head_copy] = node
        head_copy = head_copy.next

    head_copy = head
    while head_copy:
        node = nodes_map[head_copy]
        node.next = nodes_map[head_copy.next] if head_copy.next else None
        node.random = nodes_map[head_copy.random] if head_copy.random else None
        head_copy = head_copy.next

    return nodes_map[head]
    # Time complexity: O(n)
    # Space complexity: O(n)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.random = head.next.next
head.next.random = head.next.next.next
head.next.next.random = head.next.next.next.next
print(copy_list_with_random_pointer(head))
