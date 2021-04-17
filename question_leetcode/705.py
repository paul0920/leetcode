# Open hashing

class ListNode(object):

    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 997
        self.hash_set = [None] * self.size

    def key_to_index(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return

        index = self.key_to_index(key)
        node = ListNode(key)
        head = self.hash_set[index]

        if not head:
            self.hash_set[index] = node

            return

        # Insert the latest node in the front of the list
        node.next = head
        self.hash_set[index] = node

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            return

        index = self.key_to_index(key)
        node = self.hash_set[index]

        # Remember to create a dummy node
        pre_node = ListNode()
        pre_node.next = node

        while node:
            if node.key == key:
                # Check whether there is only one node
                if not pre_node.key:
                    self.hash_set[index] = node.next

                    return

                break

            pre_node = node
            node = node.next

        pre_node.next = node.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.key_to_index(key)
        node = self.hash_set[index]

        while node:
            if node.key == key:
                return True

            node = node.next

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
