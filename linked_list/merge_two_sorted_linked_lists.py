from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


def merge_two_sorted_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    sorted_list = dummy

    while list1 and list2:
        if list1.val < list2.val:
            sorted_list.next = list1
            sorted_list = list1
            list1 = list1.next
        else:
            sorted_list.next = list2
            sorted_list = list2
            list2 = list2.next

    if list1 is None:
        sorted_list.next = list2
    elif list2 is None:
        sorted_list.next = list1

    return sorted_list.next


# print(
#     mergeTwoLists(
#         ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(5)))
#     )
# )
