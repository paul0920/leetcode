
def rightSideView(self, root):
    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right, depth+1)
            collect(node.left, depth+1)
    view = []
    collect(root, 0)
    return view
