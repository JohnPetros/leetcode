from binary_tree import BinaryTree, Node


def maximum_depth_of_binary_tree(node: Node):
    if node is None:
        return 0

    left = maximum_depth_of_binary_tree(node.left)
    right = maximum_depth_of_binary_tree(node.right)

    return max(left, right) + 1


tree = BinaryTree()
tree.insert_many([3, 9, 20, 15, 7])
# tree.insert_many([1, None, 2])

print(tree)
print(maximum_depth_of_binary_tree(tree.root))
