class ListNode(object):

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dummy = ListNode()
        self.tail = self.dummy
        self.capacity = capacity
        self.key_to_prev_node = {}

    def extend_list(self, node):
        self.tail.next = node
        self.key_to_prev_node[node.key] = self.tail
        self.tail = node

    # Change prev -> node -> next -> ... -> tail
    # to prev -> next -> ... -> tail -> node
    def kick_to_last(self, prev_node):
        curr_node = prev_node.next
        prev_node.next = curr_node.next

        if prev_node.next:
            self.key_to_prev_node[prev_node.next.key] = prev_node
            # Remember to remove the pointer. Otherwise, it gets a loop in the list
            curr_node.next = None

        else:
            self.tail = prev_node

        self.extend_list(curr_node)

    def pop_front(self):
        # Update the pointers and hash table
        head = self.dummy.next
        del self.key_to_prev_node[head.key]

        self.dummy.next = head.next
        self.key_to_prev_node[head.next.key] = self.dummy

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_prev_node:
            return -1

        prev_node = self.key_to_prev_node[key]
        curr_node_value = prev_node.next.value
        self.kick_to_last(prev_node)

        return curr_node_value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_prev_node:
            prev_node = self.key_to_prev_node[key]
            self.kick_to_last(prev_node)
            self.tail.value = value

            return

        node = ListNode(key, value)
        self.extend_list(node)

        # Check whether it is out of the capacity limit
        if len(self.key_to_prev_node) > self.capacity:
            self.pop_front()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
