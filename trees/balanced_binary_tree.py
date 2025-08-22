from binary_tree import BinaryTree, Node


def balanced_binary_tree(root: Node):
    is_balanced = [True]

    def traversal(node: Node):
        if node is None:
            return 0

        left_height = traversal(node.left)

        if is_balanced[0] is False:
            return 0

        right_height = traversal(node.right)

        if abs(left_height - right_height) > 1:
            is_balanced[0] = False
            return 0

        return 1 + max(left_height, right_height)

    traversal(root)

    return is_balanced
    # Time Complexity: O(n)
    # Space Complexity: O(h)


tree = BinaryTree()
tree.insert_many([1, 2, 2, 3, 3, None, None, 4, 4])

print(balanced_binary_tree(tree.root))
