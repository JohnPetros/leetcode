from binary_tree import BinaryTree, Node


def binary_tree_inorder_traversal(root: Node):
    nodes = []

    def inorder_traversal(node: Node):
        if node is None:
            return

        if node.left:
            inorder_traversal(node.left)
        nodes.append(node.value)
        if node.right:
            inorder_traversal(node.right)

    inorder_traversal(root)

    return nodes


tree = BinaryTree()
tree.insert_many([1, None, 2, 3])
print(binary_tree_inorder_traversal(tree.root))
