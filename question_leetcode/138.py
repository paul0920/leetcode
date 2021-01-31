from collections import defaultdict
from see_node import *


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


a = [1, 2, 3, 4, 5]
head = c_node(a)
p_node(head)

# defaultdict() takes functions such as list, int
box = defaultdict(lambda: Node(0))

# This sets for the case of cur.next = None
box[None] = None

cur = head

while cur:
    box[cur].next = box[cur.next]
    box[cur].val = cur.val
    # box[cur].random = box[cur.random]
    cur = cur.next

p_node(box.get(head))
