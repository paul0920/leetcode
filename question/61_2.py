from see_node import *

a = [1, 2]
k = 2

head = c_node(a)
p_node(head)
print ""

if not head or not head.next or k == 0:
    p_node(head)

slow = fast = head
i = 0

# Fast forward k nodes and
# this is the window between
# (number of nodes) slow & fast
while i < k:

    if fast.next:
        fast = fast.next

    else:
        fast = head
        k %= i + 1
        i = -1

    p_node(fast)
    i += 1

# Locate the section, which will be cut and
# moved to the beginning of the list
while fast.next:
    slow = slow.next
    fast = fast.next

fast.next = head
head = slow.next
slow.next = None

# The following statement is incorrect
# head, slow.next, fast.next = slow.next, None, head

print ""
p_node(head)
