from binary_tree import BinaryTree, Node


def same_tree(root1: Node, root2: Node) -> bool:
    is_same_tree = [True]

    def check_same_tree(node1: Node, node2: Node):
        if node1.value != node2.value:
            is_same_tree[0] = False
            return False

        if not check_same_tree(node1.left, node2.left):
            return False

        if not check_same_tree(node1.right, node2.right):
            return False

        return True

    return is_same_tree[0]


tree1 = BinaryTree([1, 2, 3])
tree2 = BinaryTree([1, 2, 3])

print(same_tree(tree1.root, tree2.root))
