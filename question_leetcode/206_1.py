
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):

    print "head:", head.val
    print "*********"

    if not head or not head.next:
        print "......Returning......"
        print ""
        return head

    print "head.next", head.next.val
    print ""

    node = reverseList(head.next)

    print "node:", node.val
    print "head:", head.val

    print "......Reversing......"
    head.next.next = head

    print "head.next:", head.next.val
    print "NEW  head.next.next:", head.next.next.val

    # Break the connection to the original next node
    head.next = None

    print ""

    return node


a = [1, 2, 3, 4]
b = [1, 3, 4]

print "Linked List: ",

for i in a:
    print i, "->",
print "None"
print ""

l1_head = l1 = ListNode(a[0])
l2_head = l2 = ListNode(b[0])

for n in a[1:]:

    l1.next = ListNode(n)
    l1 = l1.next

for n in b[1:]:

    l2.next = ListNode(n)
    l2 = l2.next

m = reverseList(l1_head)

print "Linked List: ",

while m:
    print m.val, "->",
    m = m.next
print "None"
