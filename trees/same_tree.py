from binary_tree import BinaryTree, Node


def same_tree(root1: Node, root2: Node) -> bool:
    def check_same_tree(node1: Node, node2: Node):
        if node1 is None and node2 is not None:
            return False

        if node1 is not None and node2 is None:
            return False

        if node1 is not None and node2 is not None:
            if node1.value != node2.value:
                return False

            if not check_same_tree(node1.left, node2.left):
                return False

        return True

    return check_same_tree(root1, root2)
    # Time Complexity: O(n + m)
    # Space Complexity: O(h_p + h_q)


tree1 = BinaryTree([1, 2, 1])
tree2 = BinaryTree([1, 1, 2])

print(same_tree(tree1.root, tree2.root))
