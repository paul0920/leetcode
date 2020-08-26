from see_node import *

a = [1, 2, 3, 4, 5]
head = c_node(a)
p_node(head)
print ""

def swap(head):

    if not head or not head.next:
        return head

    new_head = head.next.next
    head, head.next = head.next, head

    head.next.next = swap(new_head)

    return head

print ""
p_node(swap(head))
