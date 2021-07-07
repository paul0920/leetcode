import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists:
        return None

    dummy_head = head = ListNode()
    heap = []

    for node in lists:  # put every head of each linked-list into heap
        if node:
            heapq.heappush(heap, (node.val, node))

    while heap:
        value, node = heapq.heappop(heap)

        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))

        head.next = node
        head = head.next

    head.next = None  # close the linked-list in case of a cycle in this list

    return dummy_head.next
