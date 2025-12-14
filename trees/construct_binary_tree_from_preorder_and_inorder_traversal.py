from binary_tree import Node


def construct_binary_tree_from_inorder_and_postorder_traversal(
    inorder: list[int],
    postorder: list[int],
):
    if not inorder or not postorder:
        return None

    root = Node(postorder.pop())

    def traversal(inorder: list[int], postorder: list[int]):
        node = Node(postorder.pop())
        node_index = inorder.index(node.value)
        root.right = traversal(inorder[node_index + 1 :], postorder)
        root.left = traversal(inorder[:node_index], postorder)
        return node

    traversal(inorder, postorder)
    return root


print(
    construct_binary_tree_from_inorder_and_postorder_traversal(
        [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
    )
)
