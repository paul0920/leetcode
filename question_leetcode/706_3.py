class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        # bucket = (key array list, value array list)
        self.buckets = [([], []) for _ in range(self.size)]

    def get_hash_code(self, key):
        return key % self.size

    def get_bucket(self, key):
        hash_code = self.get_hash_code(key)
        bucket = self.buckets[hash_code]

        for idx, k in enumerate(bucket[0]):
            if k == key:
                return idx, bucket

        return -1, bucket

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        idx, bucket = self.get_bucket(key)

        if idx == -1:
            bucket[0].append(key)
            bucket[1].append(value)

        else:
            bucket[1][idx] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx, bucket = self.get_bucket(key)

        if idx == -1:
            return -1

        return bucket[1][idx]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        idx, bucket = self.get_bucket(key)

        if idx != -1:
            bucket[0].pop(idx)
            bucket[1].pop(idx)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
