from heap._min_heap import MinHeap
from _linked_list import LinkedList
from _node import Node


def merge_k_sorted_lists(lists: list[Node]):
    heap = MinHeap()

    for index, node in enumerate(lists):
        if node:
            heap.push((node.value, index))
            lists[index] = node.next

    dummy_node = Node()
    current_node = dummy_node

    while heap:
        node_value, index = heap.pop()
        current_node.next = Node(node_value)
        current_node = current_node.next

        if lists[index]:
            heap.push((lists[index].value, index))
            lists[index] = lists[index].next

    return dummy_node.next


lists = [LinkedList(1, 4, 5).head, LinkedList(1, 3, 4).head, LinkedList(2, 6).head]
print(merge_k_sorted_lists(lists))
