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

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left is not None:
            self.postorder_traversal(node.left)

        if node.right is not None:
            self.postorder_traversal(node.right)

        print(node, end=" ")

    def get_height(self, node=None):
        if node is None:
            node = self.root

        left_height = 0
        right_height = 0

        if node.left:
            left_height = self.get_height(node.left)
        if node.right:
            self.right_height = self.get_height(node.right)

        if left_height > right_height:
            return left_height + 1
        return right_height + 1

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

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
        return " -> ".join(result)
