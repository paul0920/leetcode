# Time complexity: O(n+m), n & m are sizes of each list
# Space complexity: O(n+m), n & m are sizes of each list


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):

    if not l1:
        return l2

    elif not l2:
        return l1

    elif l1.val < l2.val:

        l1.next = mergeTwoLists(l1.next, l2)
        return l1

    else:

        l2.next = mergeTwoLists(l1, l2.next)
        return l2


a = [1, 2, 4]
b = [1, 3, 4]

l1_head = l1 = ListNode(a[0])
l2_head = l2 = ListNode(b[0])

for n in a[1:]:

    l1.next = ListNode(n)
    l1 = l1.next

for n in b[1:]:

    l2.next = ListNode(n)
    l2 = l2.next

m = mergeTwoLists(l1_head, l2_head)

while m:
    print m.val
    m = m.next
