from see_node import *

a = [1, 2, 3, 4, 5, 6]
k = 3

head = c_node(a)
p_node(head)
print ""

if not head or not head.next:
    p_node(head)

dummy = ListNode(0)
pre = dummy
dummy.next = cur = head
count = 0

while cur:
    cur = cur.next
    count += 1

print "list length:", count

m = k % count

if not k or not m:
    p_node(head)
    exit()

cur = dummy.next

for _ in range(count - m):
    pre = pre.next
    cur = cur.next

temp = dummy.next
dummy.next = cur
pre.next = None

for _ in range(m - 1):
    cur = cur.next

cur.next = temp


print ""
p_node(dummy.next)
