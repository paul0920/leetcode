# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Node is right before the intersection
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    while head != slow:
        head = head.next
        slow = slow.next

    # Node is at the intersection
    return slow
