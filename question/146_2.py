class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _append(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        p = node.prev
        t = node.next
        p.next = t
        t.prev = p

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self._remove(self.dict[key])
            self._append(self.dict[key])

            return self.dict[key].value

        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self._remove(self.dict[key])
            self._append(self.dict[key])
            self.dict[key].value = value

        else:
            if len(self.dict) == self.capacity:
                del self.dict[self.head.next.key]
                self._remove(self.head.next)

            self.dict[key] = Node(key, value)
            self._append(self.dict[key])


capacity = 2
key = 10
value = 100

obj = LRUCache(capacity)
obj.put(key, value)
print obj.get(key)
print obj.get(200)
