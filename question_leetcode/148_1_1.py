# Bottom-Up method

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getSize(head):

    if not head:
        return 0

    count = 0

    while head:
        head = head.next
        count += 1

    return count

def split(head, idx):

    i = 1
    while head and i < idx:
        head = head.next
        i += 1

    if not head:
        return head

    temp, head.next = head.next, None

    return temp

def merge(head, l, r):

    cur = head

    while l and r:

        if l.val < r.val:
            cur.next = l
            l = l.next

        else:
            cur.next = r
            r = r.next

        cur = cur.next

    # Remember the following codes
    # Move to the last node or
    # keep adding nodes from L group"
    cur.next = l if l else r

    while cur.next:
        cur = cur.next

    return cur


a = [5, 3, 7, 0, 3, 4, 2]

print "Linked List: ",

for i in a:
    print i, "->",
print "None"
print ""

head = l1 = ListNode(a[0])

for n in a[1:]:

    l1.next = ListNode(n)
    l1 = l1.next

dummy = ListNode(0)
dummy.next = head
bs = 1

times = getSize(head)

while bs < times:

    cur = dummy.next
    tail = dummy

    while cur:
        l = cur
        r = split(l, bs)
        cur = split(r, bs)
        tail = merge(tail, l, r)

    bs <<= 1


print "Linked List: ",

while dummy.next:
    print dummy.next.val, "->",
    dummy = dummy.next
print "None"
