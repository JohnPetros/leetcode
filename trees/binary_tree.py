class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return

        print(node, end=" ")

        if node.left is not None:
            self.preorder_traversal(node.left)

        if node.right is not None:
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.inorder_traversal(node.left)

        print(node, end=" ")

        if node.right is not None:
            self.inorder_traversal(node.right)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if node.left is None:
            node.left = Node(value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def insert_many(self, values):
        for value in values:
            self.insert(value)

    def __str__(self):
        if self.root is None:
            return "Empty tree"

        result = []

        def preorder_string(node):
            if node is None:
                return
            result.append(str(node))
            preorder_string(node.left)
            preorder_string(node.right)

        preorder_string(self.root)
        return " ".join(result)
