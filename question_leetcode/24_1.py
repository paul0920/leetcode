from see_node import *

a = [1, 2, 3, 4, 5]
head = c_node(a)
p_node(head)
print ""

dummy = ListNode(0)
prev = dummy
dummy.next = cur = head

while cur and cur.next:

    temp = cur.next.next
    cur.next.next = cur

    prev.next = cur.next
    cur.next = temp

    # p_node(prev)

    prev = cur
    cur = cur.next

    # p_node(prev)
    # print ""

print ""
p_node(dummy.next)
