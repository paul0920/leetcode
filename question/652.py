import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)


box = collections.defaultdict(list)
res = []

def walk(node):

    if not node:
        return 'Null'

    # Need to add something such as "-" among nodes to differentiate with the same combinations
    key = str(node.val) + "-" + str(walk(node.left)) + "-" + str(walk(node.right))
    box[key].append(node)

    # print key

    return key


walk(root)

for k, val in box.items():

    if len(val) > 1:
        res.append(box[k][0])

# for k, v in box.items():
#     print k
#     print v
#     print ""

print res
