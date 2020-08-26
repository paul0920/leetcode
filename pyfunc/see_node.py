
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def c_node(arr):

    dummy = ListNode(0)
    dummy.next = node = ListNode(arr[0])

    for n in arr[1:]:
        node.next = ListNode(n)
        node = node.next

    return dummy.next

def p_node(head):

    if not head:
        print "!!! No Nodes !!!"

    while head:
        print head.val, "->",
        head = head.next

    print "Null"
