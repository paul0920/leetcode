# Bottom-Up method

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getSize(head):
    counter = 0
    while head is not None:
        counter += 1
        head = head.next
    return counter

def split(head, step):
    i = 1
    while i < step and head:
        head = head.next
        i += 1

    if head is None:
        return None

    # Disconnect
    if head.next:
        print "head.next:", head.next.val
    else:
        print "!!! No head.next, nothing to disconnect !!!"

    temp, head.next = head.next, None

    if temp:
        print "temp:", temp.val

    return temp

def merge(head, l, r):

    cur = head

    while l and r:
        if l.val < r.val:
            cur.next, l = l, l.next
        else:
            cur.next, r = r, r.next
        cur = cur.next

    cur.next = l if l is not None else r

    # Process the case that node count is less than bs
    # For example, bs = 4, node = 3 -> 4 -> None
    while cur.next is not None:
        print "Move to the last node and/or keep adding nodes from L group"
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


size = getSize(head)
bs = 1
dummy = ListNode(0)
dummy.next = head
l, r, tail = None, None, None

while bs < size:

    print "========== bs:", bs, "============="
    print "==========", bs, "vs.", bs, "(", bs + bs, ") =========="

    # Refresh cur & tail
    cur = dummy.next
    tail = dummy

    print "========== Refreshing cur & tail =========="

    while cur:

        l = cur
        print "l:", l.val
        print ""

        print "Disconnecting", l.val, "from R........"
        r = split(l, bs)

        if r:
            print "r:", r.val

        else:
            print "!!! No r !!!"
        print ""

        print "Disconnecting R from future cur........"

        cur = split(r, bs)

        if cur:
            print "cur:", cur.val
        else:
            print "!!! No cur !!!"
        print ""

        print "Merging L & R and attaching nodes back........"
        tail = merge(tail, l, r)
        print ""

        check = dummy.next
        while check:
            print check.val, "->",
            check = check.next
        print "Null"

        print "========== Complete 1 round =========="
        print ""

    # bs = bs << 1
    bs <<= 1


print "Linked List: ",

while dummy.next:
    print dummy.next.val, "->",
    dummy = dummy.next
print "None"
