# Top-Down method
from see_node import *

def merge(l, r):

    dummy = cur = ListNode(0)

    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next

        else:
            cur.next = r
            r = r.next

        cur = cur.next

    cur.next = l if l else r

    p_node(dummy.next)

    return dummy.next

def sort(head):

    # Be careful about the "not" usage. The following statement is wrong!
    # if not head or head.next:
    if not head or not head.next:
        return head

    prev, slow, fast = None, head, head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    print "prev:", prev.val, "-> None"
    prev.next = None
    mid = slow

    print "head:", head.val

    left = sort(head)

    print "*************"
    print "mid:", mid.val
    if fast:
        print "fast:", fast.val
    else:
        print "fast: None"

    right = sort(mid)

    return merge(left, right)


# a = [3, 2, 1]
a = [5, 4, 3, 2, 1]

head = c_node(a)

print "Linked List:",
p_node(head)
print ""

cur = sort(head)

print ""
print "Linked List:",
p_node(cur)
