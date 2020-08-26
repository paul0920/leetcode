# Time complexity: O(N logk)
# N = number of nodes in the final linked list
# k = number of linked lists
# The comparison cost will be reduced to O(logk) for every pop and insertion
# to priority queue. But finding the node with the smallest value just costs
# O(1) time.

import Queue


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(self, lists):

    head = point = ListNode(0)
    q = Queue.PriorityQueue()

    for l in lists:
        if l:
            q.put((l.val, l))

    # Total is N nodes
    while not q.empty():

        # O(1)
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next

        if node:

            # O(logk)
            q.put((node.val, node))

    return head.next
