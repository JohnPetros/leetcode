from binary_tree import BinaryTree, Node


def balanced_binary_tree(root: Node):
    is_balanced = [True]

    def height(node):
        if node is None:
            return 0

        left_height = height(node.left)

        if not is_balanced[0]:
            return 0

        right_height = height(node.right)

        print(left_height, right_height)

        if abs(left_height - right_height) > 1:
            is_balanced[0] = False
            return 0

        return 1 + max(left_height, right_height)

    height(root)

    return is_balanced[0]
    # Time Complexity: O(n)
    # Space Complexity: O(h)


tree = BinaryTree()
tree.insert_many([1, 2, 3, None, None, 4, None, 5])

print(balanced_binary_tree(tree.root))
