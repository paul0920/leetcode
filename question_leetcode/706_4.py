# Open hashing

class ListNode(object):

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 997
        self.hash_list = [None for _ in range(self.size)]

    def hash_code(self, key):

        return key % self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        idx = self.hash_code(key)
        head = self.hash_list[idx]
        node = head

        if not head:
            self.hash_list[idx] = ListNode(key, value)

            return

        while node:
            if node.key == key:
                node.value = value

                return

            node = node.next

        node = ListNode(key, value)
        node.next = head.next
        head.next = node

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx = self.hash_code(key)
        node = self.hash_list[idx]

        while node:
            if node.key == key:
                return node.value

            node = node.next

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        idx = self.hash_code(key)
        node = self.hash_list[idx]

        if not node:
            return

        prev_node = ListNode()
        prev_node.next = node

        while node:
            if node.key == key:
                if not prev_node.value:
                    self.hash_list[idx] = node.next

                prev_node.next = node.next

                return

            prev_node = node
            node = node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
