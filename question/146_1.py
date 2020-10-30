import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = collections.defaultdict(int)
        self.q = collections.deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.q.remove(key)
            self.q.append(key)

            return self.dict[key]

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self.q.remove(key)

        elif len(self.dict) >= self.capacity:
            del self.dict[self.q.popleft()]

        self.dict[key] = value
        self.q.append(key)

