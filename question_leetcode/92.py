from see_node import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head, m, n):

    dummy = ListNode(0)
    dummy.next = head
    cur, prev = head, dummy

    for _ in range(m - 1):
        prev = prev.next
        cur = cur.next

    print prev.val, "prev"
    print cur.val, "cur"

    for _ in range(n - m):

        m = prev

        print "***************"
        print "prev:", prev.val, "cur:", cur.val

        temp = cur.next
        print temp.val, "temp <- cur.next"

        cur.next = temp.next
        print cur.next.val, "cur.next <- temp.next"

        temp.next = prev.next
        print temp.next.val, "temp.next <- prev.next"

        prev.next = temp
        print prev.next.val, "prev.next <- temp"

        p_node(m)

        print "***************"

    return dummy.next


a = [1, 2, 4, 6, 9, 10]
b = [1, 3, 4]

print a

l1_head = l1 = ListNode(a[0])
l2_head = l2 = ListNode(b[0])

for n in a[1:]:

    l1.next = ListNode(n)
    l1 = l1.next

for n in b[1:]:

    l2.next = ListNode(n)
    l2 = l2.next

m = reverseBetween(l1_head, 2, 4)

print "Linked List: "

while m:
    print m.val
    m = m.next
