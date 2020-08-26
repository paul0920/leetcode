# Top-Down method
from see_node import p_node

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(left, right):

    dummy = curr = ListNode(0)

    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    if left:
        curr.next = left
    elif right:
        curr.next = right

    p_node(dummy.next)

    return dummy.next

def sort(head):

    if not head or not head.next:
        return head

    # Split
    slow, fast, pre = head, head, None
    while fast and fast.next:

        pre = slow
        slow = slow.next
        print "slow:", slow.val

        fast = fast.next.next

        if fast:
            print "fast:", fast.val
        else:
            print "fast: None"
        print ""

    # Disconnect nodes after the middle node
    pre.next = None
    print "************************"

    mid = slow

    print "head:", head.val
    left = sort(head)

    print "mid:", mid.val
    right = sort(mid)

    return merge(left, right)


a = [5, 4, 3, 2, 1]

print "Linked List: ",

for i in a:
    print i, "->",
print "None"
print ""

head = l1 = ListNode(a[0])

for n in a[1:]:

    l1.next = ListNode(n)
    l1 = l1.next

dummy = sort(head)


print "Linked List: ",
p_node(dummy.next)
