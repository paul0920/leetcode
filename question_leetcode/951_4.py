# Iterative version: DFS



def flipEquiv(root1, root2):

    stk1, stk2 = [root1], [root2]

    while stk1 and stk2:
        node1, node2 = stk1.pop(), stk2.pop()

        if node1 == node2 == None:
            continue

        elif not node1 or not node2 or node1.val != node2.val:
            return False

        if node1.left == node2.left == None or node1.left and node2.left and node1.left.val == node2.left.val:
            stk1.extend([node1.left, node1.right])

        else:
            stk1.extend([node1.right, node1.left])

        stk2.extend([node2.left, node2.right])

    return not stk1 and not stk2
