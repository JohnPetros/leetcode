from binary_tree import BinaryTree, Node

#          3
#         /  \
#        E    5
#       / \  /
#      I   R A
#         / \  \
#        N   C  V
#             \
#              S
# I N S C R E V A 5 3

tree = BinaryTree()
n1 = Node("I")
n2 = Node("N")
n3 = Node("S")
n4 = Node("C")
n5 = Node("R")
n6 = Node("E")
n7 = Node("V")
n8 = Node("A")
n9 = Node("-")
n10 = Node("5")
n0 = Node("3")

n0.left = n6
n0.right = n10
n6.left = n1
n6.right = n5
n5.left = n2
n5.right = n4
n4.right = n3
n9.left = n8
n8.right = n7
n10.right = n9

tree.root = n0

tree.postorder_traversal()
