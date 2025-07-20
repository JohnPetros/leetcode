from tree import BinaryTree, Node


tree = BinaryTree()
# tree.insert_many([3, 5, 7, 11, 13, 7, 17, 19])
# tree.insert_many([11, 7, 3, 19, 13, 7, 17, 5])


tree.insert_many([19, 13, 17, 7, 11, 3, 7, 5])

is_type_one = False
is_type_two = False


def traversal(parent: Node = None, node: Node = None):
    if node is None:
        return

    if parent and node.value > parent.value:
        global is_type_one
        is_type_one = True

    if parent and node.value < parent.value:
        global is_type_two
        is_type_two = True

    traversal(node, node.left)


traversal(None, tree.root)

if (is_type_one and is_type_two) or (not is_type_one and not is_type_two):
    print("0")
else:
    print("1" if is_type_one else "2")
