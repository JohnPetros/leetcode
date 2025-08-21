from binary_tree import BinaryTree, Node


def diameter_of_binary_tree(root: Node):
    largest_diameter = [0]

    def get_height(node: Node):
        if node is None:
            return 0

        left_height = get_height(node.left)
        right_height = get_height(node.right)
        diameter = left_height + right_height

        largest_diameter[0] = max(diameter, largest_diameter[0])

        return 1 + max(left_height, right_height)

    get_height(root)
    return largest_diameter[0]
    # Time Complexity: O(n)
    # Space Complexity: O(h)


tree = BinaryTree()
tree.insert_many([1, 2, 3, 4, 5])

print(diameter_of_binary_tree(tree.root))
