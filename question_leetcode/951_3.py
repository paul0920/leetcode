# Iterative version: BFS

import collections

def flipEquiv(root1, root2):

    dq1, dq2 = map(collections.deque, ([root1], [root2]))

    while dq1 and dq2:
        node1, node2 = dq1.popleft(), dq2.popleft()

        if node1 == node2 == None:
            continue

        elif not node1 or not node2 or node1.val != node2.val:
            return False

        # Check the left child and see whether the are the same
        if node1.left == node2.left == None or node1.left and node2.left and node1.left.val == node2.left.val:
            dq1.extend([node1.left, node1.right])

        # If left child is different, check the right child later on
        else:
            dq1.extend([node1.right, node1.left])

        dq2.extend([node2.left, node2.right])

    # return not dq1 and not dq2
    return True
