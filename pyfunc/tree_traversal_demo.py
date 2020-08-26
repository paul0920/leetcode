# Tree traversal

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print str(root.val) + " ->",
        # Traverse right
        inorder(root.right)

def preorder(root):

    if root:
        # Traverse root
        print str(root.val) + " ->",
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)

def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print str(root.val) + " ->",


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.left.right.left = Node(6)
root.right.left = Node(6)
root.right.right = Node(7)

print "In-order traversal"
inorder(root)
print "Null"

print "\nPre-order traversal"
preorder(root)
print "Null"

print "\nPost-order traversal"
postorder(root)
print "Null"
