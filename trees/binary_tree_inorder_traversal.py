from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return str(self.to_list())

    def to_list(self):
        result = []
        queue = deque([self])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result


def build_tree(values):
    if not values or values[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    children = nodes[::-1]
    root = children.pop()

    for node in nodes:
        if node:
            if children:
                node.left = children.pop()
            if children:
                node.right = children.pop()
    return root


def binary_tree_inorder_traversal(root: TreeNode) -> list[int]:
    nodes = []

    def inorder_traversal(current_node: TreeNode, nodes: list[int]):
        if current_node:
            inorder_traversal(current_node.left, nodes)
            nodes.append(current_node.val)
            inorder_traversal(current_node.right, nodes)

    inorder_traversal(root, nodes)

    return nodes


tree = build_tree([1, None, 2, 3])

print(binary_tree_inorder_traversal(tree))
