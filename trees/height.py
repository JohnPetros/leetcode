from binary_tree import BinaryTree, Node


tree = BinaryTree()
n1 = Node("I")
n2 = Node("N")
n3 = Node("S")
n4 = Node("C")
n5 = Node("R")
n6 = Node("E")
n7 = Node("V")
n8 = Node("A")
n9 = Node("5")
n0 = Node("3")

n0.left = n6
n0.right = n9
n6.left = n1
n6.right = n5
n5.left = n2
n5.right = n4
n4.right = n3
n9.left = n8
n8.right = n7

tree.root = n0

print("height ->", tree.get_height())
